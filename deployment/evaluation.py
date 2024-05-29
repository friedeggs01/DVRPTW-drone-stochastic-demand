from gp.node.function import *
from gp.node.terminal import *
from copy import deepcopy
# from gp.population.gp import *
from gp.population.individual import *
from data.read_data import *
from utils.utils import *
from .deploy_request import *
from graph.network import Network

def calFitness_three_policies(indi: Individual, network: Network, request_list):
    # storing processing history
    network_copy = deepcopy(network)
    request_list_copy = deepcopy(request_list)
    sum_request = len(request_list_copy)

    # Execution time slot
    T = request_list_copy[0].arrival
    reject = 0 # number of reject request
    cost_sum = 0 # sum of cost of all request that excuted 
    while len(request_list_copy) > 0:
        request_processing, reject_request, reject1 = get_request_run(request_list_copy, 0, T)
        for request in request_processing:
            request_list_copy.remove(request)
        for request in reject_request:
            request_list_copy.remove(request)
        reject = reject + reject1

        request_decision = []
        # Calculate value of GP for each request
        for request in request_processing:
            
            # decide the request is accepted or rejected
            value_of_decision_gp = decision_gp(T)
            if value_of_decision_gp < 0:
                reject = reject + 1
                continue
            
            # choose the truck-drone own the highest gp-value
            value_of_choosing_gp = {}
            for i in range(network_copy.num_vehicle):
                value_of_choosing_gp[i] = (choosing_gp(indi, request, T, network_copy, network_copy.trucks[i], network_copy.drones[i]))
            key_with_highest_value = max(value_of_choosing_gp, key=value_of_choosing_gp.get)
            
            # find the route by insert new customer into existed route of the truck-drone
            if len(network.routes[key_with_highest_value]) < 2:
                index = network.routes[key_with_highest_value].index(10000)
                network.routes[key_with_highest_value].insert(index, request.customer_id)
                
                if (len(network.routes[key_with_highest_value]) == 1):
                     request.serving_start = network.links[0][network.routes[key_with_highest_value][0]].dist / network.trucks[key_with_highest_value].velocity
                if (len(network.routes[key_with_highest_value]) == 2):
                    request.serving_start = network.links[network.routes[key_with_highest_value][0]][network.routes[key_with_highest_value][1]].dist / network.trucks[key_with_highest_value].velocity
                request.serving_end = request.serving_start + request.service_time
                
                for t in range(request.serving_start, request.serving_end):
                    network.trucks[key_with_highest_value].remain_capacity[t] -= request.customer_demand
                cost_sum += network.update_cost(key_with_highest_value)
            elif request.drone_serve == True and network.check_constraint(request, key_with_highest_value):
                index = network.routes[key_with_highest_value].index(10000)
                network.routes[key_with_highest_value].insert(index, request.customer_id)
                network.routes[key_with_highest_value].append(request.customer_id)
            elif network.check_constraint(request):
                network.routes[key_with_highest_value].append(request.customer_id)
                cost_sum += network.update()
            
        T = T + 1
    return cost_sum



# route [2, 3, 4, 5, 6, 1000, 4]
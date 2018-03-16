import math
import heapq


class KNN(object):
    # initalize KNN
    def __init__(self, data_set: list = [], k=2, ref_point=(0, 0)):
        super(KNN, self).__init__()
        self.ref_point = ref_point
        self.k = k
        self.data_set = data_set

    # calculate eucledian distance from reference point to data point
    def getDistance(self, data_point):
        distance = math.sqrt((self.ref_point[0] - data_point[0]) ** 2 + (self.ref_point[1] - data_point[1]) ** 2)
        return distance

    # format the data set and save into dictionary
    def formatData(self):
        formatted_data = []

        for data_point in self.data_set:
            point_dict = {"coordinates": data_point, "distance": self.getDistance(data_point)}
            formatted_data.append(point_dict)

        return formatted_data

    # solve KNN
    def solve(self):
        formatted_data = self.formatData()
        k_nearest_neighbors = heapq.nsmallest(self.k, formatted_data, key=lambda x: x['distance'])
        return k_nearest_neighbors


def getDistance(data_point, reference):
    distance = math.sqrt((reference[0] - data_point[0]) ** 2 + (reference[1] - data_point[1]) ** 2)
    # print("DATAPOINT-REFERENCE-DISTANCE", data_point, "-", reference, "-", distance)
    return distance


def range_search(query_node, moving_objects, range):
    range_list = list()
    for object in moving_objects:
        if object == query_node: continue
        eucl_dis = getDistance(object, query_node)
        if eucl_dis <= range:
            range_list.append(object)
    return range_list


def lemma1(dis_pq, dis_pki, dis_qi):
    if (dis_pq + dis_qi <= dis_pki):
        return True
    else:
        return False

    # Validation


def validate(query_node, peer_node, knn_list_dic):
    dpq = 0.0
    dqi = 0.0
    dpki = 0.0
    # coordinateDistlist = []
    length = len(knn_list_dic)
    returnlist=[]
    # Find the distances
    dpq = getDistance(peer_node, query_node)
    dpki = knn_list_dic[len(knn_list_dic) - 1]['distance']

    # Now for KNN of peer_node
    for item in knn_list_dic:
        # coordinateDistlist.append(getDistance(query_node, item['coordinates']))
        dic = {'p':peer_node,'q': query_node , 'IO':item['coordinates'],'valid':lemma1(dpq,dpki,getDistance(query_node, item['coordinates'])),'distfromquerynode':getDistance(query_node, item['coordinates'])}
        returnlist.append(dic)
    return returnlist





        # interested_objects = [(3, 21), (3, 24), (7, 23), (2, 18), (6, 17), (6, 15),(7,12),(13,15),(15,18),(20,20),(17,15),(22,17),(23,12),(18,11),(18,10),(18,9)]
        # moving_object = [(7,18),(4,22),(10,20),(3,15),(10,14),(17,18),(19,14),(21,14),(18,12),(8,9),(4,5),(8,2),(14,2)]


if __name__ == "__main__":

    interested_objects = [(3, 21), (3, 24), (7, 19), (2, 18), (6, 17), (6, 15), (7, 12), (13, 15), (15, 18)]
    moving_objects = [(7, 18), (4, 22), (10, 20), (3, 15), (10, 14)]

    # Need A  Range Search Here which return a list
    peer_result = list()
    validate_list = []
    query_node = (7, 18)
    range = 6.0
    k = 3
    K = 5
    peer_result = range_search(query_node, moving_objects, range)
    print("Range Search revealed these points in Range:",peer_result)
    print("For each coordinate in range showing their", k, "Nearest Neighbour")
    for item in peer_result:
        knn = KNN(interested_objects, k, item)
        knn_list_dic = knn.solve()
        len_dic = len(knn_list_dic)

        print("For peer:", item,k, "NN:", knn_list_dic)

        for dict_item in knn_list_dic:
            validate_list = validate(query_node, item, knn_list_dic)

        print(validate_list)
        print()     

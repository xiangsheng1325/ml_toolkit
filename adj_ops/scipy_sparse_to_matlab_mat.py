import scipy.io as sio


def save_matlab_graph(dump_fname, sp_adj, graphname="scipy_sparse_graph"):
    dump_data = {'G': sp_adj, 'graphname': graphname}
    sio.savemat(dump_fname, dump_data)


def load_matlab_graph(fname):
    tmp_data = sio.loadmat(fname)
    #print(tmp_data)
    return tmp_data['G']


if __name__ == '__main__':
    import networkx as nx
    g = nx.grid_2d_graph(3, 3)
    sp_adj = nx.adjacency_matrix(g)
    save_matlab_graph("test.mat", sp_adj)
    matlab_adj = load_matlab_graph("test.mat")
    print(matlab_adj)

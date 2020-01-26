import trimesh
import slam.io as sio
import slam.topology as stop
import slam.plot as splt
import slam.generate_parametric_surfaces as sps
import numpy as np
from vispy.scene import Line
from visbrain.objects import VispyObj, SourceObj

if __name__ == '__main__':
    """ mesh_boundary works fine    
    # here is how to get the vertices that define the boundary of an open mesh
    K = [1, 1]
    open_mesh = sps.generate_quadric(K, nstep=20)
    print('================= mesh_boundary =================')
    print('Identify the vertices lying on the boundary of the mesh and order'
          'them to get a path traveling across boundary vertices')
    print('The output is a list of potentially more than one boudaries '
          'depending on the topology of the input mesh')
    open_mesh_boundary = stop.mesh_boundary(open_mesh)
    print(open_mesh_boundary)
    print('Here the mesh has a single boundary')
 
    # WARNING : BrainObj should be added first before
    visb_sc = splt.visbrain_plot(mesh=open_mesh, caption='open mesh')
    # create points with vispy
    for bound in open_mesh_boundary:
        points = open_mesh.vertices[bound]
        s_rad = SourceObj('rad', points, color='red', symbol='square',
                          radius_min=10)
        visb_sc.add_to_subplot(s_rad)
        lines = Line(pos=open_mesh.vertices[bound], width=10, color='b')
        # wrap the vispy object using visbrain
        l_obj = VispyObj('line', lines)
        visb_sc.add_to_subplot(l_obj)
    visb_sc.preview()
    """
    # # here is how to get the vertices that define the boundary of
    # # a texture on a mesh
    mesh = sio.load_mesh('data/example_mesh.gii')
    tex_parcel = sio.load_texture('data/example_texture_parcel.gii')
    boundary = stop.texture_boundary(mesh, tex_parcel.darray[0], 0)
    print(boundary)
    # plot
    visb_sc2 = splt.visbrain_plot(mesh=mesh, tex=tex_parcel.darray[0],
                                  caption='texture boundary')
    cols=['red', 'green', 'yellow', 'blue']
    ind=0
    for bound in boundary:
        s_rad = SourceObj('rad', mesh.vertices[bound], color=cols[ind], symbol='square',
                          radius_min=10)
        ind+=1
        if ind==len(cols):
            ind=0
        visb_sc2.add_to_subplot(s_rad)
        #lines = Line(pos=mesh.vertices[bound], color=trimesh.visual.random_color(), width=10)
        # wrap the vispy object using visbrain
        #l_obj = VispyObj('line', lines)
        #visb_sc2.add_to_subplot(l_obj)
        path_visual = trimesh.load_path(mesh.vertices[bound])
        path_visual.vertices_color = trimesh.visual.random_color()
        # points = mesh.vertices[bound]
        # cloud_boundary = trimesh.points.PointCloud(points)
        # cloud_colors = np.array([trimesh.visual.random_color()
        #                          for i in points])
        # cloud_boundary.vertices_color = cloud_colors
        # scene_list.append(cloud_boundary)
    visb_sc2.preview()
    boundary_vertices = stop.texture_boundary_vertices(tex_parcel.darray, 0,
    mesh.vertex_neighbors)
    print(boundary_vertices)
    path_visual = trimesh.load_path(mesh.vertices[boundary[3]])
    # create a scene with the mesh, path, and points
    scene = trimesh.Scene([path_visual, mesh ])

    # trimesh.points.plot_points(points)
    # plt.show()

    # col = mesh.visual.vertex_colors
    # col[:, 3] = 100
    # mesh.visual.vertex_colors = col
    # scene_list.append(path_visual)
    # print(path_visual)
    # scene = trimesh.Scene(scene_list)
    # scene.show(smooth=False)

    """ cut_mesh works fine!!
    print('================= cut_mesh =================')
    print('Cut he mesh into subparts corresponding to the different values in '
          'the texture tex_parcel')
    parc_u = np.unique(tex_parcel.darray[0])
    print('Here the texture contains {0} different values: {1}'
          ''.format(len(parc_u), parc_u))
    sub_meshes, sub_tex, sub_corresp = stop.cut_mesh(mesh,
                                                     tex_parcel.darray[0])
    print('The order of the resulting submeshes is given by'
          ' the second ouput: {}'.format(sub_tex))
    print('The respective indices of the vertices of each submesh in the '
          'original mesh before the cut is given by the third output:')
    print(sub_corresp)

    scene_list = list()

    # joint_mesh = sub_meshes[0] + sub_meshes[1]
    # joint_tex = np.ones((joint_mesh.vertices.shape[0],))
    # joint_tex[:sub_meshes[0].vertices.shape[0]] = 10
    joint_mesh = sub_meshes[0]
    joint_tex = np.zeros((sub_meshes[0].vertices.shape[0],))
    last_ind=sub_meshes[0].vertices.shape[0]
    for ind, sub_mesh in enumerate(sub_meshes[1:]):
        sub_tex = np.ones((sub_mesh.vertices.shape[0],)) * (ind + 1)
        joint_mesh += sub_mesh
        joint_tex = np.hstack((joint_tex, sub_tex))
    visb_sc = splt.visbrain_plot(mesh=joint_mesh, tex=joint_tex, caption='mesh parts shown in different colors')
    visb_sc.preview()
    """

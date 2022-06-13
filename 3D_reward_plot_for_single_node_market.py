import numpy as np
import matplotlib.pyplot as plt

# Importing the figure data
x_axis = np.load('./3D_plots_of_AIRL/x_axis_valus.npy')
y_axis = np.load('./3D_plots_of_AIRL/y_axis_valus.npy')
z_axis_true_reward  = np.load('./3D_plots_of_AIRL/z_axis_values_true_reward.npy')
z_axis_learned_reward  = np.load('./3D_plots_of_AIRL/z_axis_values_learned_reward.npy')


# Start Ploting
fig = plt.figure()
fig.set_size_inches(17,9)

# Ploting True Reward 
true_rew_fig = fig.add_subplot(1,2,1,projection='3d')
true_rew_fig.set_ylabel('Load (GW)')
true_rew_fig.set_xticklabels(["0","0","100","200","300","400","500","600"])
true_rew_fig.set_xlabel('Quantity Offer (MW)')
true_rew_fig.set_zlabel('Reward Value')
true_rew_fig.set_title('True Reward')
true_rew_fig.plot_wireframe(x_axis,y_axis,z_axis_true_reward,color='green',label='True Reward')

# Ploting Learned Reward 
learned_rew_fig = fig.add_subplot(1,2,2,projection='3d')
learned_rew_fig.set_ylabel('Load (GW)')
learned_rew_fig.set_xlabel('Quantity Offer (MW)')
learned_rew_fig.set_xticklabels(["0","0","100","200","300","400","500","600"])
learned_rew_fig.set_zlabel('Reward Value')
learned_rew_fig.set_title('Learned Reward')
learned_rew_fig.plot_wireframe(x_axis,y_axis,z_axis_learned_reward,color='blue',label='Learned Reward')


plt. show()

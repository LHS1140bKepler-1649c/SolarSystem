import numpy as np
import matplotlib.pyplot as plt

G = 9.6743015*(10**(-11))

class Object:
    def __init__(self, x, y, v_x, v_y, delta_t, other_wight):
        self.other_weight = other_wight
        self.x = x
        self.y = y
        self.v_x_0 = v_x
        self.v_y_0 = v_y
        self.delta_t = delta_t
        self.r = self.get_r()
        self.one_over_r_3 = self.get_one_over_r_3()
        self.a_x = self.get_a_x()
        self.a_y = self.get_a_y()
        self.v_x = self.v_x_0 + self.a_x*(self.delta_t / 2)
        self.v_y = self.v_y_0 + self.a_y*(self.delta_t / 2)

    def get_r(self):
        return np.sqrt(self.x**2 + self.y**2)

    def get_one_over_r_3(self):
        return 1 / (self.r**3)

    def get_a_x(self):
        return -((G*self.other_weight*self.x) / (self.r**3))

    def get_a_y(self):
        return -((G*self.other_weight*self.y) / (self.r**3))

    def get_v_x(self):
        return self.v_x + self.a_x*self.delta_t

    def get_v_y(self):
        return self.v_y + self.a_y*self.delta_t

    def get_x(self):
        return self.x + self.v_x*self.delta_t

    def get_y(self):
        return self.y + self.v_y*self.delta_t

    def update(self):
        self.x = self.get_x()
        self.y = self.get_y()
        self.r = self.get_r()
        self.one_over_r_3 = self.get_one_over_r_3()
        self.a_x = self.get_a_x()
        self.a_y = self.get_a_y()
        self.v_x = self.get_v_x()
        self.v_y = self.get_v_y()

    def __repr__(self):
        return f'x: {self.x} \ny: {self.y}'

    def get_trajectory(self):
        return (self.x, self.y)


    


if __name__ == '__main__':
    Earth = Object(150000000000, 0.0, 0.0, 30000, 100, 1.989*(10**30))
    x = list()
    y = list()
    # print(Earth)
    # print('---------------------')
    for _ in range(1000000):
        Earth.update()
        trajectory = Earth.get_trajectory()
        x.append(trajectory[0])
        y.append(trajectory[1])
        # print(Earth)
        # print('---------------------')
    plt.plot(x,y)
    plt.grid()
    plt.show()
from polynomial import db
import numpy as np

class Domain(db.Model):

    __tablename__ = 'domain'
    id = db.Column(db.Integer, primary_key = True)
    domain0 = db.Column(db.Float)
    domain1 = db.Column(db.Float)

    def __init__(self, domain0 = 0, domain1 = 2*np.pi):
        self._domain0 = domain0
        self._domain1 = domain1
        self._interval = np.linspace(domain0,domain1,1000)
        self._point = (domain0 + domain1)*(1/2)

    @property
    def domain0(self):
        return self._domain0
    @domain0.setter
    def domain0(self, domain0):
        self._domain0 = domain0
        self._interval = np.linspace(self._domain0, self._domain1,1000)
    @property
    def domain1(self):
        return self._domain1
    @domain1.setter
    def domain1(self, domain1):
        self._domain1 = domain1
        self._interval = np.linspace(self._domain0, self._domain1,1000)
    @property
    def interval(self):
        return self._interval

    def construct_limit_right(self, theta):
        return [theta + 1(1/i) for i in range(1,100)]
    def construct_limit_left(self, theta):
        return [theta - 1(1/i) for i in range(1,100)]

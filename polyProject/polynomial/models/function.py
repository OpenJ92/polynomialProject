import plotly.plotly as py
import plotly.graph_objs as go
from polynomial import db, np

class Function(db.Model):

    __tablename__ = 'function'
    id = db.Column(db.Integer, primary_key = True)

    def __init__(self, terms):
        self._terms = []
        self._domain = []

        for i in terms:
            if type(i) == list:
                self._terms = self._terms + i
                if i.domain not in self._domain:
                    self._domain = self._domain + i.domain
            else:
                self._terms.append(i)
                if i.domain not in self._domain:
                    self._domain = self.domain + [i.domain]


    def __add__(self, other):
        return Function([self, other])

    @property
    def terms(self):
        return self._terms
    @property
    def domain(self):
        return self._domain

    def evaluate_point(self, theta = 0):
        return (theta, sum([term.evaluate_point(theta)[1] for term in self.terms]))
    def evaluate_interval(self, theta_A = 0, theta_B = 6*np.pi, dtheta = 1000):
        return [self.evaluate_point(theta) for theta in np.linspace(theta_A,theta_B,dtheta)]
    def plot(self):
        trace0 = go.Scatter(x=[_tuple[0] for _tuple in self.evaluate_interval()],y=[_tuple[1] for _tuple in self.evaluate_interval()])
        return py.plot([trace0], filename = 'basic-line', auto_open=True)

import plotly.plotly as py
import plotly.graph_objs as go
from polynomial import db, np
from polynomial.models.function import Function
from polynomial.models.domain import Domain

class Cos(db.Model):

    __tablename__ = 'cos'
    id = db.Column(db.Integer, primary_key = True)
    coefficent = db.Column(db.Float)
    frequency = db.Column(db.Float)

    def __init__(self, domain = Domain(),  coefficent = 1, frequency = 1):
        self._domain = domain
        self._coefficent = coefficent
        self._frequency = frequency
    def __add__(self, other):
        return Function([self, other])
    def __mul__(self, other):
        if isinstance(other, float):
            self._coefficent = self._coefficent * other
        if isinstance(other, int):
            self._coefficent = self._coefficent * other
    def __rmul__(self, other):
        if isinstance(other, float):
            self._coefficent = self._coefficent * other
        if isinstance(other, int):
            self._coefficent = self._coefficent * other

    @property
    def terms(self):
        return self
    @property
    def domain(self):
        return self._domain
    @property
    def coefficent(self):
        return self._coefficent
    @property
    def frequency(self):
        return self._frequency

    def evaluate_point(self, theta):
        return (theta, self.coefficent*np.cos(self.frequency*theta))
    def evaluate_interval(self):
        return [self.evaluate_point(theta) for theta in self.domain.interval]
    def plot(self):
        trace0 = go.Scatter(x=[_tuple[0] for _tuple in self.evaluate_interval()],y=[_tuple[1] for _tuple in self.evaluate_interval()])
        return py.plot([trace0], filename = 'basic-line', auto_open=True)

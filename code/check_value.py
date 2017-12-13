import random

from checks import AgentCheck
class MyCheck(AgentCheck):
  def check(self, instance):
    self.gauge('Badr.my_metric', random.randint(0, 1000))

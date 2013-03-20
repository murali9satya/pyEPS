from ...utils.io import IoService
from ...utils.statemachine import StateMachine
from ...utils.config import Configuration
from ...nodes.mme.states import Default

# Configuration data model
# {
#  "system": {
#   "mmeName": str(),
#   "servedGummeis": [(str(), tuple()), ...],
#   "maximumEnbsAllowed": int(),
#  },
#  "s1": {
#   "s1SetupTimeToWait": int(),
#  },
# }

class Mme(StateMachine):

    def __init__(self, name, port, configData):
        super(Mme, self).__init__()
        self.ioService = IoService(name, port)
        self.config = Configuration(configData, self.ioService)

    def execute(self):
        self.ioService.addIncomingMessageCallback(self.handleIncomingMessage)
        self.ioService.start()
        self.changeState(Default)

    def terminate(self):
        self.ioService.stop()

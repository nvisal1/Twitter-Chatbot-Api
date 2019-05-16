from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load('./models/current/nlu')

x = interpreter.parse(u"Show me tweets from @united in the last three weeks mentioning about the environment")
print(x)
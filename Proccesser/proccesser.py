import os
from datetime import time
import datetime

from django.contrib.messages.storage import default_storage

from django.conf import settings
from .recolor import Core


def proccessImage(type,input_path):
    # print(+input_path)


    try:
        # input_path = os.path.join(settings.BASE_DIR, input_path)
        input_path = os.path.join("files", input_path)
        output_path = input_path.replace("uploads/", "outputs/")
        # input_path=default_storage.location = output_path
        # input_path="/files/"+input_path




        if type == 'protanopia':
            Core.simulate(input_path=input_path,
                      return_type='save',
                      save_path=output_path,
                      simulate_type='protanopia',
                      simulate_degree_primary=0.9)
            return output_path
        elif type == 'deutranopia':

            Core.simulate(input_path=input_path,
                      return_type='save',
                      save_path=output_path,
                      simulate_type='deutranopia',
                      simulate_degree_primary=0.9)
            return output_path

        # Simulating Tritanopia with diagnosed degree of 0.9 and saving the image to file.
        elif type == 'tritanopia':
            Core.simulate(input_path=input_path,
                      return_type='save',
                      save_path=output_path,
                      simulate_type='tritanopia',
                      simulate_degree_primary=0.9)
            return output_path

        elif type == 'hybrid':
            Core.simulate(input_path=input_path,
                      return_type='save',
                      save_path=output_path,
                      simulate_type='hybrid',
                      simulate_degree_primary=0.5,
                      simulate_degree_sec=0.5)
            return output_path
        else:
            return None
    except Exception as e:
        print(e)
        return None






# if __name__ == '__main__':
# proccessImage('protanopia','files/uploads/CAP3829895643117645055.jpg')
#     proccessImage()
import logging

logging.basicConfig(level=logging.INFO)

class ComplexNumberCalculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add(self, num1, num2):
        self.logger.info("Adding numbers {} and {}".format(num1, num2))
        real_part = num1[0] + num2[0]
        imag_part = num1[1] + num2[1]
        result = (real_part, imag_part)
        self.logger.info("Result: {}".format(result))
        return result

class Tools:
    """
    various data processing tools
    """
    @staticmethod
    def splitArray(array, count):
        """
        split the array into parts
        :param array: current array
        :param count: number of elements in one part
        :return: array of arrays
        """
        arr_general = []
        start = 0
        end = count
        while True:
            if len(array[start:end]) == 0: break
            arr_general.append(array[start:end])
            start = end
            end += end
        return arr_general

if __name__ == '__main__':
    print(Tools.__doc__)
import numpy
import scipy
import matplotlib.pyplot as plt


def getExecutionTimes(file):
    times = []
    with open(file, 'r') as f:
        for line in f:
            if line.startswith('Execution time: '):
                times.append(float(line.split(' ')[2]))
                print(float(line.split(' ')[2]))
    return times


def plotExecutionTimes(times):
    # plot the data
    x = numpy.array(range(1, len(times) + 1))
    y = numpy.array(times)
    plt.scatter(x, y, label='Times', color='blue')
    plt.xlabel('Size')
    plt.ylabel('Time (seconds)')
    plt.title('Execution times')
    popt = scipy.optimize.curve_fit(lambda t, a, b: a * 2 ** (2 ** (b * t)), x, y)
    print("here")
    plt.plot(x, popt[0][0] * 2 ** (2 ** (popt[0][1] * x)),
             label='fit: %.5f*2^(2^(%.5f*size))' % tuple(popt[0]), color='red')
    plt.legend()
    plt.savefig('./execution_times2.png')
    plt.show()


if __name__ == '__main__':
    plotExecutionTimes(getExecutionTimes('../graphs-second-try.txt'))

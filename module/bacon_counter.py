from mrjob.job import MRJob
class Bacon_count(MRJob): # Create a class called Bacon_count
   def mapper(self, _, line): #  mapper()function that will take (self, _, line)
       for word in line.split(): # Call the split() method on each line to break the text into a list of words.
           if word.lower() == "bacon": # will convert to lowercase.
               yield "bacon", 1 # If the words match the search word "bacon," a key-value pair will show as yield "bacon", 1.

   def reducer(self, key, values):
       # self parameter is used in Python to represent the instance of the class.
       # key parameter represents the key of the key-value pair created in the mapper function. In this example, the key is "bacon."
       # values parameter is a list of values created in the mapper function
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()

#However, there are a couple of scenarios where low-level APIs might apply:
#You need finely tuned control over the data in your clusters that high-level APIs can't provide.
#Your role involves maintaining legacy code that uses low-level APIs.




# The driver is the heart of the application. It is responsible for maintaining the application information; responding to the code or input; and analyzing, distributing, and scheduling work to the executors.

# The executors perform the code assigned by the driver and then report the state of the computation to the driver.

# The cluster manager controls the driver and executors and allocates resources to the machines on the Spark applications. The cluster manager is an external service for acquiring resources on the cluster. Spark can either use it's own standalone cluster manager that comes standard with Spark or another application (e.g., Apache Mesos, Hadoop YARN).

# Each executor needs to work on each partition for perfect parallelism, as shown below:


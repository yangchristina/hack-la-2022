import matplotlib.pyplot as plt
import get_started

data = get_started.get_student_and_current_score()
student = data.keys()
score = data.values()
data = get_started.get_actors_with_post_message_length()
actor = data.keys()
length = data.values()

plt.bar(score, length)
plt.savefig("mygraph.png")


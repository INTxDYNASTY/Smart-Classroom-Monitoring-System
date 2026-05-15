import csv
import time

def save_data(
    attention,
    sleep,
    phone,
    total_students,
    attentive_students,
    not_attentive_students,
    feedback
):

    with open("data.csv", mode="a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            time.strftime("%H:%M:%S"),
            attention,
            sleep,
            phone,
            total_students,
            attentive_students,
            not_attentive_students,
            feedback
        ])
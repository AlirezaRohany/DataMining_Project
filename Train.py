import Read_Records

records = Read_Records.all_records
training_records = []
for i in range(len(records)):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        training_records.append(records[i])

cancelled_training_records = []
not_cancelled_training_records = []

i = 0
for record in training_records:
    if int(training_records[i].is_cancelled) == 1:
        cancelled_training_records.append(training_records[i])
    if int(training_records[i].is_cancelled) == 0:
        not_cancelled_training_records.append(training_records[i])
    i += 1

P_is_cancelled_in_train = len(cancelled_training_records) / len(training_records)
P_is_not_cancelled_in_train = len(not_cancelled_training_records) / len(training_records)
import random
import statistics
import timeit
import numpy
import pandas as pd
import csv

correct = 1

def get_std_dev(ls):
    n = len(ls)
    mean = sum(ls) / n
    var = sum((x - mean)**2 for x in ls) / n
    std_dev = var ** 0.5
    return std_dev


with open('./outlier4.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Simple average n = 11 with outlier removal, 4 % errors")
    e = 0.1
    elapsed_list = []
    stdt = []
    avg1 = []
    outlier = []
    avg2 = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 96:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)

            std = get_std_dev(inputs)

            avg = sum(inputs)/len(inputs)

            sample2 = []
            for value in inputs:
                if value <= avg + 3 * std and value >= avg - 3 * std:
                    sample2.append(value)

            avg = sum(sample2)/len(sample2)

            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))


with open('./outlier40.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Simple average n = 11 with outlier removal, 40 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 60:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            std = get_std_dev(inputs)
            avg = sum(inputs)/len(inputs)
            sample2 = []
            for value in inputs:
                if value <= avg + 3 * std and value >= avg - 3 * std:
                    sample2.append(value)
            avg = sum(sample2)/len(sample2)
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))


with open('./outlier100.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Simple average n = 11 with outlier removal, 100 % errors")

    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err >= 0:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            std = get_std_dev(inputs)
            avg = sum(inputs)/len(inputs)
            sample2 = []
            for value in inputs:
                if value <= avg + 3 * std and value >= avg - 3 * std:
                    sample2.append(value)
            avg = sum(sample2)/len(sample2)
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./weighted4.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Weighted average n = 11, 4 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 96:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            dists = []
            for j in range(11):
                dists.append([])
                for k in range(11):
                    if j != k:
                        dists[j].append(abs(inputs[j]-inputs[k]))
            scales = []
            for j in range(11):
                scales.append(1)
                for k in range(10):
                    scales[j] *= dists[j][k]**2
            weights = []
            for j in range(11):
                weights.append(1/1+scales[j])
            s = sum(weights)
            avg = 0
            for j in range(11):
                avg += weights[j]/s*inputs[j]
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./weighted40.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Weighted average n = 11, 40 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 60:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            dists = []
            for j in range(11):
                dists.append([])
                for k in range(11):
                    if j != k:
                        dists[j].append(abs(inputs[j]-inputs[k]))
            scales = []
            for j in range(11):
                scales.append(1)
                for k in range(10):
                    scales[j] *= dists[j][k]**2
            weights = []
            for j in range(11):
                weights.append(1/1+scales[j])
            s = sum(weights)
            avg = 0
            for j in range(11):
                avg += weights[j]/s*inputs[j]
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./weighted100.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Weighted average n = 11, 100 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err >= 0:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            dists = []
            scales = []
            weights = []
            avg = 0
            for j in range(11):
                dists.append([])
                for k in range(11):
                    if j != k:
                        dists[j].append(abs(inputs[j]-inputs[k]))
                scales.append(1)
                for k in range(10):
                    scales[j] *= dists[j][k]**2
                weights.append(1/1+scales[j])

            s = sum(weights)

            for j in range(11):
                avg += weights[j]/s*inputs[j]
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))



def group(groups, value):
    if groups == []:
        groups.append([value])
        return groups
    else:
        for i in range(len(groups)):
            if value >= 0.95 * (sum(groups[i])/len(groups[i])) and value <= 1.05 * (sum(groups[i])/len(groups[i])):
                groups[i].append(value)
                return groups
        groups.append([value])
        return groups

with open('./byzantine4.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Approximate Byzantine voting n = 11, 4 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 96:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            # Group values based on group avg
            groups = []
            for value in inputs:
                groups = group(groups, value)
            # Count the size of groups vs sample size
            avg = 10
            for i in range(len(groups)):
                if len(groups[i]) > (2/3)*len(inputs):
                    avg = sum(groups[i])/len(groups[i])
                    break
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./byzantine40.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Approximate Byzantine voting n = 11, 40 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > 60:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            # Group values based on group avg
            groups = []
            for value in inputs:
                groups = group(groups, value)
            # Count the size of groups vs sample size
            avg = 10
            for i in range(len(groups)):
                if len(groups[i]) > (2/3)*len(inputs):
                    avg = sum(groups[i])/len(groups[i])
                    break
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./byzantine100.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['magnitude', 'correctness', 'elapsed'])
    print("Approximate Byzantine voting n = 11, 100 % errors")
    e = 0.1
    elapsed_list = []
    while e < 1.1:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err >= 0:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            # Group values based on group avg
            groups = []
            for value in inputs:
                groups = group(groups, value)
            # Count the size of groups vs sample size
            avg = 10
            for i in range(len(groups)):
                if len(groups[i]) > (2/3)*len(inputs):
                    avg = sum(groups[i])/len(groups[i])
                    break
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For e = {e} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([e, round(count/10000*100, 2), round(elapsed, 3)])
        e += 0.1
        e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))
"""
####################################################################################
"""
with open('./outlier.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['frequency', 'correctness', 'elapsed'])
    #print("Simple average n = 11 with outlier removal, 4 % errors")
    e = 0.3
    freq = 100
    elapsed_list = []
    stdt = []
    avg1 = []
    outlier = []
    avg2 = []
    while freq >= 0:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > freq:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)

            std = get_std_dev(inputs)

            avg = sum(inputs)/len(inputs)

            sample2 = []
            for value in inputs:
                if value <= avg + 3 * std and value >= avg - 3 * std:
                    sample2.append(value)

            avg = sum(sample2)/len(sample2)

            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For f = {100-freq} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([100-freq, round(count/10000*100, 2), round(elapsed, 3)])
        freq -= 2
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./weighted.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['frequency', 'correctness', 'elapsed'])
    print("Weighted average n = 11, 4 % errors")
    e = 0.3
    freq = 100
    elapsed_list = []
    while freq >= 0:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > freq:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            dists = []
            for j in range(11):
                dists.append([])
                for k in range(11):
                    if j != k:
                        dists[j].append(abs(inputs[j]-inputs[k]))
            scales = []
            for j in range(11):
                scales.append(1)
                for k in range(10):
                    scales[j] *= dists[j][k]**2
            weights = []
            for j in range(11):
                weights.append(1/1+scales[j])
            s = sum(weights)
            avg = 0
            for j in range(11):
                avg += weights[j]/s*inputs[j]
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For f = {100-freq} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([100-freq, round(count/10000*100, 2), round(elapsed, 3)])
        freq -= 2
        #e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

with open('./byzantine.csv', 'w') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['frequency', 'correctness', 'elapsed'])
    print("Approximate Byzantine voting n = 11, 4 % errors")
    e = 0.3
    freq = 100
    elapsed_list = []
    while freq >= 0:
        start_time = timeit.default_timer()
        count = 0
        for i in range(10000):
            inputs = []
            for j in range(11):
                err = random.uniform(0, 100)
                if err > freq:
                    inputs.append(random.uniform(correct - e, correct + e))
                else:
                    inputs.append(correct)
            # voter implementation
            # Group values based on group avg
            groups = []
            for value in inputs:
                groups = group(groups, value)
            # Count the size of groups vs sample size
            avg = 10
            for i in range(len(groups)):
                if len(groups[i]) > (2/3)*len(inputs):
                    avg = sum(groups[i])/len(groups[i])
                    break
            # check correctness
            if avg > correct*0.99 and avg < correct*1.01:
                count += 1
        elapsed = timeit.default_timer() - start_time
        elapsed_list.append(elapsed)
        print(f"For f = {100-freq} , {round(count/10000*100, 2)}% of 10000 outputs are 99% correct, elapsed time: {round(elapsed, 3)} seconds")
        csv_writer.writerow([100-freq, round(count/10000*100, 2), round(elapsed, 3)])
        freq -= 2
        #e = round(e, 1)
    print("Avg elapsed time = " + str(sum(elapsed_list)/len(elapsed_list)))

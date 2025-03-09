# Read file
file = open('input.txt', 'r')
lines = file.readlines()

fin = []

for line in lines:
    temp = []
    line = line.split()
    for idx, num in enumerate(line):
        if idx == len(line)-1:
            num = num.replace('\n', '')
        temp.append(int(num))
    fin.append(temp)

# Need to find cases where the numbers are uniformly increasing or decreasing, and where they change between 1 and 3. My idea here is to add those that pass to a final list which is then checked, since iterating oer the same list twice seems inefficient.
safe_reports = []

for report in fin:
    checks = {'dec': False,
              'inc': False,
              'all_in_bounds': True}
    
    for idx, num in enumerate(report):
        if idx != 0:
            prev = report[idx-1]

            if prev < num:
                checks['dec'] = True
            if prev > num:
                checks['inc'] = True
            if abs(prev - num) > 3 or abs(prev - num) < 1:
                checks['all_in_bounds'] = False
        
    if checks['dec'] != checks['inc'] and checks['all_in_bounds'] == True:
        safe_reports.append(report)

print(len(safe_reports))

# Part 2 is trickier. By definition, the reports that are in safe_reports must have failed, so just iterate over each element of each of them and try removing it.
for report in fin:
    if report not in safe_reports:
        for popper in range(0, len(report)):
            checks = {'dec': False,
                      'inc': False,
                      'all_in_bounds': True}
            temp_report = report.copy()
            del temp_report[popper]

            for idx, num in enumerate(temp_report):
                if idx != 0:
                    prev = temp_report[idx-1]

                    if prev < num:
                        checks['dec'] = True
                    if prev > num:
                        checks['inc'] = True

                    if abs(prev - num) > 3 or abs(prev - num) < 1:
                        checks['all_in_bounds'] = False
                    
            if checks['dec'] != checks['inc'] and checks['all_in_bounds'] == True:
                safe_reports.append(temp_report)
                break
print(len(safe_reports))

def input_to_lists():
    f = open("input.txt","r")
    res = []
    for line in f:
        l = []
        for elt in line.split():
            l.append(int(elt))
        res.append(l)
    return res

res = input_to_lists()

def safe_report(l):
    report = l
    is_safe = True
    j = 1
    is_increasing = report[j] > report[j - 1]
    while(j < len(report) and is_safe):
        if is_increasing:
            if report[j] > report[j-1] and report[j] - report[j-1] <= 3:
                j += 1
            else:
                is_safe = False
        else:
            if report[j] < report[j-1] and report[j-1] - report[j] <= 3:
                j += 1
            else:
                is_safe = False
    return is_safe


def safe_reports(l):
    ans = 0
    for i in range(len(l)):
        ans += safe_report(l[i])
    return ans

def safe_reports_with_removal(l):
    ans = 0
    for i in range(len(l)):
        report = l[i]
        if safe_report(report):
            ans += 1
        else:
            for i in range(len(report)):
                report_c = report.copy()
                report_c.pop(i)
                if safe_report(report_c):
                    ans += 1
                    break
    return ans


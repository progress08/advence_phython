import json

def process_student_grades(f_in, f_out):
    f = open(f_in)
    data = json.load(f)
    f.close()
    
    lst = []
    for s in data:
        ns = s.copy()
        g = s.get('grades', [])
        if len(g) > 0:
            avg = sum(g)/len(g)
        else:
            avg = 0
        ns['average_grade'] = round(avg, 2)
        lst.append(ns)
        
    o = open(f_out, 'w')
    json.dump(lst, o, indent=4)
    o.close()
    print("Processing complete. Updated data saved to "+f_out)

if __name__ == "__main__":
    process_student_grades("students.json", "students_analyzed.json")

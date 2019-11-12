tactics = {'impact': 'TA0040', 'defense-evasion': 'TA0005', 'lateral-movement': 'TA0008', 'privilege-escalation': 'TA0004', 'credential-access': 'TA0006', 'discovery': 'TA0007', 'collection': 'TA0009', 'exfiltration': 'TA0010', 'command-and-control': 'TA0011', 'execution': 'TA0002', 'persistence': 'TA0003', 'initial-access': 'TA0001'}

f=open('lol.txt')
data=f.readlines()
techlist=list()
for line in data:
    line=line.strip()
    techlist.append(line)

for tech in techlist:
    techid = tech.split()[-1]
    technique = "".join(x+"-" for x in tech.split("-")[:-1])[:-1]
    tactic = "".join(x+"-" for x in tech.split("-")[-1].split()[:-1])[:-1]
    tacticid = tactics[tactic]
    url = "https://attack.mitre.org/techniques/"+techid
    print '{{"technique": "{}", "technique_id": "{}", "url": "{}", "tactic": "{}", "tactic-id": "{}"}},'.format(technique, techid, url, tactic, tacticid)
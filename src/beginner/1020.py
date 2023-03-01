days = int(input(""))

years = days // 365
days -= years * 365

months = days // 30
days -= months * 30

print(f"{years} ano(s)\n{months} mes(es)\n{days} dia(s)")
surrounding_16=[0,1,4,5,3,2,3,5,0,1,4,5,3,2,3,5]
surrounding_8=[0,1,4,5,3,2,3,5]
total_heat=0
for i in surrounding_8:
    if i>1:
        total_heat=total_heat+(i-1)
        print(i)
for i in surrounding_16:
    if i>2:
        total_heat=total_heat+(i-2)
cell_assc_heat=0
cell_assc_heat=cell_assc_heat+total_heat
print(total_heat)
avg_heat_level_env = sum(surrounding_8)/len(surrounding_8)
# if type == "home":
heat_difference = avg_heat_level_env - cell_assc_heat
cell_assc_heat += heat_difference*0.4
print(cell_assc_heat)

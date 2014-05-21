import relay
import Cdf
import myplot
results = "http://coolrunning.com/results/10/ma/Apr25_27thAn_set1.shtml"

results = relay.ReadResults(url=results)

def convert_speeds_to_time(speed):
    khm =  speed * 1.609344
    time = (10/khm) * 60
    minute = int(time)
    second = int((time - minute)*60)
    return  '{m}:{s}'.format(
                    m=minute,
                    s=second
            )

def get_place(results, column=0):
    return [int(result[column]) for result in results]

def total_percentile_rank(results, place=97):
    places = get_place(results)
    places.sort(reverse=True)
    print(places)
    cdf = Cdf.MakeCdfFromList(places,is_sorted=True)
    return cdf, cdf.Prob(place)

def GetSpeeds_F2039(results):
    return GetSpeeds_with_div(results, 'F2039')


def GetSpeeds_M4049(results):
    return GetSpeeds_with_div(results, 'M4049')

def GetSpeeds_M5059(results):
    return GetSpeeds_with_div(results, 'M5059')

def GetSpeeds_with_div(results, div_range):
    speeds = []
    for (place, divtot, div, gun, net, pace) in results:
        if not div_range == div:continue
        speed = relay.ConvertPaceToSpeed(pace)
        speeds.append(speed)
    return speeds




def main():
    #cdf, place = total_percentile_rank(results)
    speeds = relay.GetSpeeds(results)
    speed = relay.ConvertPaceToSpeed('6:53')
    cdf = Cdf.MakeCdfFromList(speeds)
    print cdf.Prob(speed),'speed'
    print convert_speeds_to_time(speed),'time'
    myplot.Cdf(cdf)
    myplot.Show()
    
    speeds_old = GetSpeeds_M4049(results)
    cdf_old = Cdf.MakeCdfFromList(speeds_old)
    rank = cdf_old.Prob(speed)
    print rank,'rank', speed,'speed'
    print convert_speeds_to_time(speed),'time'
    myplot.Cdf(cdf_old)
    myplot.Show()
    
    speeds_5059 = GetSpeeds_M5059(results)
    cdf_5059 = Cdf.MakeCdfFromList(speeds_5059)
    future_speed = cdf_5059.Value(rank)
    print future_speed,'speed'
    print convert_speeds_to_time(future_speed),'time'
    myplot.Cdf(cdf_5059)
    myplot.Show()
   
    fspeeds = GetSpeeds_F2039(results)
    cdf_female = Cdf.MakeCdfFromList(fspeeds)
    fspeed = cdf_female.Value(rank)
    print fspeed,'speed'
    print convert_speeds_to_time(fspeed),'time'
    myplot.Cdf(cdf_female)
    myplot.Show()
   

if __name__ == '__main__':
    main()

def encadrement(trace,lat,lon):
    res = []
    cpt = 2
    while (cpt<len(trace)-2) and (len(res)<4):
        if (float(lat)<=float(trace[cpt]) and float(lat)>=float(trace[cpt-2])) and (float(lon)<=float(trace[cpt+1]) and float(lon)>=float(trace[cpt-1])):
            #res.append(trace[cpt-2])
            #res.append(trace[cpt-1])
            res.append(trace[cpt])
            res.append(trace[cpt+1])
        cpt += 2
    return res

def direction(pointSuivant,lat,lon,orientation):
    if (orientation>45) and (orientation<135):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                return("tout droit")
            else:
                return("demi-tour")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                return("a droite")
            else:
                return("a gauche")
    elif ((orientation>=0) and (orientation<=45)) or ((orientation>315) and (orientation<360)):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                return("a gauche")
            else:
                return("a droite")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                return("tout droit")
            else:
                return("demi-tour")
    elif (orientation>=135) and (orientation<225):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                return("a gauche")
            else:
                return("a droite")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                return("demi-tour")
            else:
                return("tout droit")
    elif (orientation>=225) and (orientation<=315):
        if abs(float(lat)-float(pointSuivant[0])) > abs(float(lon)-float(pointSuivant[1])):
            if (float(lat)-float(pointSuivant[0])) < 0:
                return("demi-tour")
            else:
                return("tout droit")
        else:
            if (float(lon)-float(pointSuivant[1])) < 0:
                return("a gauche")
            else:
                return("a droite")





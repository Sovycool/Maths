lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"

class Formule:
    
    def __init__(self,formule) -> None:

        self.initiale = formule        
        self.formule = self.transforme(formule)

    def transforme(self,formule):

        count = 0
        output = []
        x = ""
        
        while count < len(formule):

            if formule[count] == "(":
                
                if x != "":
                    output.append(x)
                    output.append(formule[count])
                    x = ""
                y = ""
                count += 1
        
                while count < len(formule) and formule[count] != ")":
                    
                    y += formule[count]
                    count += 1

                if len(output) != 0 and (type(output[-1]) == Formule or (output[-1] not in chiffres and output[-1] not in lettres)):

                    output.append("*")

                output.append(Formule(y))

            elif formule[count] not in chiffres and formule[count] not in lettres:

                    output.append(x)
                    output.append(formule[count])
                    x = ""

            else:
                
                if len(output) == 0:

                    x += formule[count]

                elif len(x) == 0:
                    
                    if type(output[-1]) == Formule:
                        
                        output.append("*")
                        x += formule[count]
                    
                    else:
                        
                        x += formule[count]

                elif x[-1] not in chiffres and formule[count] in chiffres:
                    
                    output.append(x)
                    output.append("*")
                    x = formule[count]


                elif x[-1] not in lettres and formule[count] in lettres:
                    
                    output.append(x)
                    output.append("*")
                    x = formule[count]

                else:

                    x += formule[count]

            count += 1
        
        if x != "":
            output.append(x)

        return output

    def output(self):

        output = []
        for k in self.formule:
            if type(k) == Formule:
                output.append(k.output())
            else:
                output.append(k)
        return output

f = Formule("(15+2)a/2+(18+1)")
print(f.output())


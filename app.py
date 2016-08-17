#get input from command line and create franchises
import sys, getopt
from os import path
import time
import codecs

class Franchise():
    _city = ''
    _pop = ''
    _owner = ''
    _phone = ''
    _fax = ''
    _address = ''
    _email = ''

    def __str__(self):
        return "{} {} {}".format(self.city, self.owner, self.phone)

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def pop(self):
        return self._pop

    @pop.setter
    def pop(self, pop):
        self._pop = pop

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def fax(self):
        return self._fax

    @fax.setter
    def fax(self, fax):
        self._fax = fax

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def getEnglish(self):
        return """<div class="container">
        <div class="row franchise-table-row">
          <div class="column text-right border-right">
          <strong>City, Province<br>Pop<span class="hide-in-mobile">ulation</span><span class="show-in-mobile">.</span> of City / Metro Area<br>Owner's Name<br>Phone Number<br>Fax Number<br>Address for Inquiries<br>E-mail</strong>
          </div>
          <div class="column border-left">
            <strong>{}</strong><br />
            {}<br />
            {}<br />
            {}<br />
            {}<br />
            {}<br />
            <a href="{}" class="emil" data-emil-before="{}" data-emil-after="{}">{}</a>
          </div>
        </div>""".format(self.city, self.pop, self.owner, self.phone, self.fax, self.address, self.email, self.email.split("@")[0], self.email.split("@")[1], self.email)

    def getFrench(self):
        return """  <div class="row franchise-table-row">
            <div class="column text-right border-right">
          <strong>Ville, province<br>Pop<span class="hide-in-mobile">ulation</span><span class="show-in-mobile">.</span> de Ville/Métro<br><span class="hide-in-mobile">nom du c</span><span class="show-in-mobile">C</span>oncessionnaire<br>Téléphone<br>Télécopieur<br>Adresse<br>Courriel</strong>
          </div>
          <div class="column border-left">
            <strong>{}</strong><br />
            {}<br />
            {}<br />
            {}<br />
            {}<br />
            {}<br />
            <a href="{}" class="emil" data-emil-before="{}" data-emil-after="{}">{}</a>
          </div>
        </div>""".format(self.city, self.pop, self.owner, self.phone, self.fax, self.address, self.email, self.email.split("@")[0], self.email.split("@")[1], self.email)

def parseline(line, franchise):
    try:
        cat, content = line.split(":")
        if 'city, province' in cat.lower():
            franchise.city = content.strip()
        elif 'population' in cat.lower():
            franchise.pop = content.strip()
        elif 'owner' in cat.lower():
            franchise.owner = content.strip()
        elif 'phone' in cat.lower():
            franchise.phone = content.strip()
        elif 'fax' in cat.lower():
            franchise.fax = content.strip()
        elif 'inquiries' in cat.lower():
            franchise.address = content.strip()
        elif 'e-mail' in cat.lower():
            franchise.email = content.strip()
    except ValueError:
        pass

def printCities(cities, outputfile):
    f = codecs.open(outputfile, encoding="utf-8", mode="w+") # + means create the file if it isn't already there

    f.write("ENGLISH: \n")
    f.write("\n")
    for franchise in cities:
        f.write('\n----------\n')
        f.write(franchise.getEnglish())
        f.write('\n----------\n')
    f.write("\n\n")
    f.write("FRENCH: \n")
    f.write("\n")
    for franchise in cities:
        f.write('\n----------\n')
        f.write(franchise.getFrench())
        f.write('\n----------\n')

    f.close()

def main():
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError:
        print('GetoptError!')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            inputfile = arg
        if opt == "-o":
            outputfile = arg

    if inputfile == '':
        print("No input file :( \nMake sure you designate an input file with the flag -i")
        sys.exit(2)


    try:
        currentDir = path.dirname(__file__)
        filePath = path.join(currentDir, inputfile)
        if path.exists(filePath):
            f = open(filePath)
            if f.mode == 'r':
                citycount = 0
                cities = []
                content = f.readlines()
                for line in content:
                    if "city, province" in line.lower():
                        citycount += 1
                        franchise = Franchise()
                        cities.append(franchise)
                    parseline(line, cities[citycount-1])

            f.close()
            if(outputfile == ''):
                outputfile = 'newfranchises' + str(time.time()) + '.txt'
            printCities(cities, outputfile)

        else:
            print(filepath, ": No such file.")
            sys.exit(2)
    except ValueError:
        print("couldn't read the file.")



if __name__ == '__main__':
    main()

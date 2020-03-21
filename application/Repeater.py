from datetime import datetime, date

class Repeater(object):
    def __init__(self, rptr_dict=None):
        self.__coverage_notes = []
        if rptr_dict is not None:
            self.__url = str(rptr_dict['url']) if rptr_dict['url'] is not None else None
            self.__band = str(rptr_dict['band']) if rptr_dict['band'] is not None else None
            self.__output_freq = float(rptr_dict['output_freq']) if rptr_dict['output_freq'] is not None else None
            self.__input_freq = float(rptr_dict['input_freq']) if rptr_dict['input_freq'] is not None else None
            self.__offset = str(rptr_dict['offset']) if rptr_dict['offset'] is not None else None
            self.__open = bool(rptr_dict['open']) if rptr_dict['open'] is not None else None
            self.__location = str(rptr_dict['location']) if rptr_dict['location'] is not None else None
            self.__site_name = str(rptr_dict['site_name']) if rptr_dict['site_name'] is not None else None
            self.__latitude = str(rptr_dict['latitude']) if rptr_dict['latitude'] is not None else None
            self.__longitude = str(rptr_dict['longitude']) if rptr_dict['longitude'] is not None else None
            self.__elevation = int(rptr_dict['elevation']) if rptr_dict['elevation'] is not None else None
            self.__site_name = str(rptr_dict['site_name']) if rptr_dict['site_name'] is not None else None
            self.__call_sign = str(rptr_dict['call_sign']) if rptr_dict['call_sign'] is not None else None
            self.__sponsor = str(rptr_dict['sponsor']) if rptr_dict['sponsor'] is not None else None
            self.__website = str(rptr_dict['website']) if rptr_dict['website'] is not None else None
            self.__ctcss = str(rptr_dict['ctcss']) if rptr_dict['ctcss'] is not None else None
            self.__info = str(rptr_dict['info']) if rptr_dict['info'] is not None else None
            self.__links = str(rptr_dict['links']) if rptr_dict['links'] is not None else None
            self.__features = str(rptr_dict['features']) if rptr_dict['features'] is not None else None
            self.__erp = str(rptr_dict['erp']) if rptr_dict['erp'] is not None else None
            self.__last_coordinated = str(rptr_dict['last_coordinated']) if rptr_dict['last_coordinated'] is not None else None
            self.__last_updated = str(rptr_dict['last_updated']) if rptr_dict['last_updated'] is not None else None
            if rptr_dict['coverage_notes'] is not None and len(rptr_dict['coverage_notes']) > 0:
                for coverage_note in rptr_dict['coverage_notes']:
                    self.__coverage_notes.append(coverage_note)
        else:
            self.__closed = None
            self.__input_freq = None
            self.__features = None
            self.__erp = None
            self.__last_coordinated = None
            self.__last_updated = None
            self.__website = None
            self.__latitude = None
            self.__longitude = None

            # Info
            self.__wide_area_coverage = None
            self.__autopatch = None
            self.__remote_base = None
            self.__shared = None
            self.__internet = None
            self.__portable = None       


    def is_empty(self, value):
        if isinstance(value, str):
            value.strip()
        return value if value != ' ' and value != '(none)' and value != '(None)' and value != 'N/A' else None

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = self.is_empty(value)

    @property
    def band(self):
        return self.__band

    @band.setter
    def band(self, value):
        self.__band = self.is_empty(value)

    @property
    def input_freq(self):
        return self.__input_freq

    @input_freq.setter
    def input_freq(self, value):
        self.__input_freq = self.is_empty(value)

    @property
    def output_freq(self):
        return self.__output_freq

    @output_freq.setter
    def output_freq(self, value):
        self.__output_freq = self.is_empty(value)
        if 1.800 <= self.__output_freq <= 2.000:
            self.__band = '160 Meters (1.8 Mhz)'
        elif 3.500 <= self.__output_freq <= 4.000:
            self.__band = '80 Meters (3.5 MHz)'
        elif 7.000 <= self.__output_freq <= 7.300:
            self.__band = '40 Meters (7 MHz)'
        elif 10.100 <= self.__output_freq <= 10.150:
            self.__band = '30 Meters (10.1 MHz)'
        elif 14.000 <= self.__output_freq <= 14.350:
            self.__band = '20 Meters (14 MHz)'
        elif 18.068 <= self.__output_freq <= 18.168:
            self.__band = '17 Meters (18 MHz)'
        elif 21.000 <= self.__output_freq <= 21.450:
            self.__band = '15 Meters (21 MHz)'
        elif 24.890 <= self.__output_freq <= 24.990:
            self.__band = '12 Meters (24 MHz)'            
        elif 28.000 <= self.__output_freq <= 29.700:
            self.__band = '10 Meters (28 MHz)'
        elif 50.0 <= self.__output_freq <= 54.0:
            self.__band = '6 Meters (50 MHz)'
        elif 144.0 <= self.__output_freq <= 148.0:
            self.__band = '2 Meters (144 MHz)'
        elif 219.0 <= self.__output_freq <= 225.0:
            self.__band = '1.25 Meters (222 MHz)'
        elif 420.0 <= self.__output_freq <= 450.0:
            self.__band = '70 cm (420 MHz)'
        elif 902.0 <= self.__output_freq <= 928.0:
            self.__band = '33 cm (902 MHz)'
        elif 1240.0 <= self.__output_freq <= 1300.0:
            self.__band = '23 cm (1240 MHz)'

    def __del__(self):
        self.clear()

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = self.is_empty(value)
        if self.__offset == '+600 Mhz':
            self.__input_freq = self.__output_freq + .600
        elif self.__offset == '-600 Mhz':
            self.__input_freq = self.__output_freq - .600
        else:
            self.__input_freq = self.__output_freq

    @property
    def open(self):
        return self.__open

    @open.setter
    def open(self, value):
        self.__open = self.is_empty(value)

    @property
    def closed(self):
        return self.__closed

    @closed.setter
    def closed(self, value):
        self.__closed = self.is_empty(value)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = self.is_empty(value)

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = self.is_empty(value)

    @property
    def site_name(self):
        return self.__site_name

    @site_name.setter
    def site_name(self, value):
        self.__site_name = self.is_empty(value)

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        tmp = self.is_empty(value)
        if tmp:
            tmp = tmp.split()
            self.__latitude = tmp[0].replace('(','').replace(')','').replace('°','') + tmp[1].replace('.','')

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        tmp = self.is_empty(value)
        if tmp:
            tmp = tmp.split()
            self.__longitude = tmp[0].replace('(','').replace(')','').replace('°','') + tmp[1].replace('.','')

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        self.__elevation = self.is_empty(value)

    @property
    def call_sign(self):
        return self.__call_sign

    @call_sign.setter
    def call_sign(self, value):
        self.__call_sign = self.is_empty(value)

    @property
    def sponsor(self):
        return self.__sponsor

    @sponsor.setter
    def sponsor(self, value):
        if 'ARI' in value:
            self.__sponsor = 'Amateur Radio, Incorporated'
        elif 'BARC' in value:
            self.__sponsor = 'Bridgerland Amateur Radio Club (Logan)'
        elif 'BARC' in value:
            self.__sponsor = 'Borderline Amateur Radio Club (Vernal)'
        elif 'CSERG' in value:
            self.__sponsor = 'Community Service Emergency Radio Group (Clearfield)'
        elif 'DARC' in value:
            self.__sponsor = 'Dixie Amateur Radio Club (St. George)'
        elif 'DARS' in value:
            self.__sponsor = 'Deseret Amateur Radio Society'
        elif 'DCARC' in value:
            self.__sponsor = 'Davis County Amateur Radio Club'
        elif 'EARC' in value:
            self.__sponsor = 'Elko Amateur Radio Club'            
        elif 'ERRS' in value:
            self.__sponsor = 'Emergency Radio Response System (now known as ERC)'
        elif 'ExPost1973' in value:
            self.__sponsor = 'Explorer Post #1973 (Orem)'
        elif 'GCWA' in value:
            self.__sponsor = 'Glen Canyon Wireless Association (Page, AZ)'
        elif 'GMRA' in value:
            self.__sponsor = 'Grand Mesa Repeater Association (Grand Junction, CO)'
        elif 'IREAN' in value:
            self.__sponsor = 'Intermountain Repeater Emergency Amateur Network'
        elif 'LPARG' in value:
            self.__sponsor = 'Lake Powell Amateur Radio Group'
        elif 'MARA' in value:
            self.__sponsor = 'Mercury Amateur Radio Association'
        elif 'OARC' in value:
            self.__sponsor = 'Ogden Amateur Radio Club'
        elif 'RMRA' in value:
            self.__sponsor = 'Rocky Mountain Radio Association'
        elif 'SDARC' in value:
            self.__sponsor = 'Sinbad Desert Amateur Radio Club (Carbon, Emery, Grand Counties)'                                                                        
        elif 'SLCOARES' in value:
            self.__sponsor = 'Salt Lake County Amateur Radio Emergency Service'
        elif 'SLPEAKARC' in value:
            self.__sponsor = 'Salt Lake Peaks Amateur Radio Club'
        elif 'SNP' in value:
            self.__sponsor = 'Shared -- Non-protected'
        elif 'TCARES' in value:
            self.__sponsor = 'Tooele County Amateur Radio Emergency Service'
        elif 'TCARS' in value:
            self.__sponsor = 'Tooele County Amateur Radio Society'
        elif 'UARC' in value:
            self.__sponsor = 'Utah Amateur Radio Club'
        elif 'UCRC' in value:
            self.__sponsor = 'Utah County Radio Club (now UHDARC)'
        elif 'UHDARC' in value:
            self.__sponsor = 'Utah High Desert Amateur Radio Club (Utah County)'
        elif 'UTCOARES' in value:
            self.__sponsor = 'Utah County Amateur Radio Emergency Service'
        elif 'UVARC' in value:
            self.__sponsor = 'Utah Valley Amateur Radio Club'
        elif 'UVHFS' in value:
            self.__sponsor = 'Utah VHF Society (statewide)'
        elif 'UVRMC' in value:
            self.__sponsor = 'Utah Valley Regional Medical Center'
        elif 'UVU' in value:
            self.__sponsor = 'Utah Valley University'
        elif 'YOUARK' in value:
            self.__sponsor = 'Affiliated with but not quite the same as UARC'
        else:
            self.__sponsor = self.is_empty(value)

        if '/VHFS' in value:
            self.__sponsor += ', Aligned with the Utah VHF Society'


    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, value):
        self.__website = self.is_empty(value)

    @property
    def ctcss(self):
        return self.__ctcss

    @ctcss.setter
    def ctcss(self, value):
        self.__ctcss = self.is_empty(value) 

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, value):
        self.__info = self.is_empty(value)
        if self.__info:
            # O - Designates "open" repeater or system, available for all to use.  Note that an "open" system may include a "closed" (e.g. members only) autopatch.
            if 'O' in self.__info:
                self.__open = True
            # C - Designates "closed" repeater or system.  For more information about the "how and why" of closed systems, look at the Frequency Coordination FAQ.
            if 'C' in self.__info or 'Ca' in self.__info:
                self.__closed = True            
            # X - Designates a "Wide Area Coverage" repeater.  Typically, this repeater offers unusually wide coverage, usually due to its excellent location.
            if 'X' in self.__info:
                self.__wide_area_coverage = True
            # A - Designates that this repeater has an autopatch. Note: Most autopatches are closed except to members of the supporting organization, even if the repeater itself is open. NOTE:  Where it is uncertain whether or not the autopatch is closed, it will be listed with an "A" and not a "Ca".  For more info about "closed" patches, look here.
            # Ca - Designates an autopatch that is known to be "closed" (see above).            
            if 'A' in self.__info or 'Ca' in self.__info:
                self.__autopatch = True
            # Rb - Designates "Remote Base" capability.  This usually means that there is another radio on-site that can be remotely "steered" to other frequencies, linking them to the repeater.
            if 'Rb' in self.__info:
                self.__remote_base = True
            # Snp - Shared — no protection. Designates a frequency that can be used for temporary and experimental repeaters. No protection is guaranteed from similar repeaters that may commence operation.
            if 'Snp' in self.__info:
                self.__shared = True
            # I - Internet. Designates a repeater that can be linked to other repeaters, users, and systems using “Voice Over Internet Protocol” (VOIP). This includes repeaters participating in systems such as IRLP, EchoLink, E-QSO, WIRES, etc. When available, additional information about such repeaters is carried in the “Links” column in italics.
            if 'I' in self.__info:
                self.__internet = True            
            # P - Portable. Designates a repeater which may be operated from different locations as required for emergencies and special events.
            if 'P' in self.__info:
                self.__portable = True   

    @property
    def links(self):
        return self.__links

    @links.setter
    def links(self, value):
        self.__links = self.is_empty(value)         

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        self.__features = self.is_empty(value)

    @property
    def erp(self):
        return self.__erp

    @erp.setter
    def erp(self, value):
        self.__erp = self.is_empty(value)

    @property
    def last_coordinated(self):
        return self.__last_coordinated

    @last_coordinated.setter
    def last_coordinated(self, value):
        self.__last_coordinated = self.is_empty(value)

    @property
    def last_updated(self):
        return self.__last_updated

    @last_updated.setter
    def last_updated(self, value):
        self.__last_updated = self.is_empty(value)

    @property
    def coverage_notes(self):
        return self.__coverage_notes

    @coverage_notes.setter
    def coverage_notes(self, value):
        tmp = self.is_empty(value)
        if tmp:
            self.__coverage_notes.append(tmp)

    @property
    def google_map_link(self):
        self.__google_map_link = None
        if self.__latitude and self.__longitude:
            self.__google_map_link = 'https://www.google.com/maps/place/'+self.__latitude+'+'+self.__longitude+'/'
        return self.__google_map_link

    def to_list(self):
        return [
            '=HYPERLINK("'+self.__url+'","'+self.__url+'")' if self.__url else None,
            self.__band,
            self.__output_freq,
            self.__input_freq,
            self.__offset,
            self.__open,
            self.__closed,
            self.__location,
            self.__site_name,
            self.__latitude,
            self.__longitude,
            '=HYPERLINK("'+self.google_map_link+'","'+self.google_map_link+'")' if self.google_map_link else None,
            self.__elevation,
            self.__call_sign,
            self.__sponsor,
            '=HYPERLINK("'+self.__website+'","'+self.__website+'")' if self.__website else None,
            self.__ctcss,
            self.__info,
            self.__links,
            self.__wide_area_coverage,
            self.__autopatch,
            self.__remote_base,
            self.__shared,
            self.__internet,
            self.__portable,              
            self.__features,
            self.__erp,
            self.__last_coordinated,
            self.__last_updated,
            ' '.join(str(e) for e in self.__coverage_notes)
        ]


    def clear(self):        
        self.__url = None
        self.__band = None
        self.__output_freq = None
        self.__input_freq = None
        self.__offset = None
        self.__open = None
        self.__closed = None
        self.__location = None
        self.__site_name = None
        self.__latitude = None
        self.__longitude = None
        self.__elevation = None
        self.__call_sign = None
        self.__sponsor = None
        self.__website = None
        self.__ctcss = None
        self.__info = None
        self.__links = None
        self.__wide_area_coverage = None
        self.__autopatch = None
        self.__remote_base = None
        self.__shared = None
        self.__internet = None
        self.__portable = None         
        self.__features = None
        self.__erp = None
        self.__last_coordinated = None
        self.__last_updated = None
        self.__coverage_notes = []
        

    @staticmethod
    def column_headers():
        return [
            'url',
            'band',
            'output_freq',
            'input_freq',
            'offset',
            'open',
            'closed',
            'location',
            'site_name',
            'latitude',
            'longitude',
            'google_maps',
            'elevation',
            'call_sign',
            'sponsor',
            'website',
            'ctcss',
            'info',
            'links',
            'wide_area_coverage',
            'autopatch',
            'remote_base',
            'shared',
            'internet',
            'portable',            
            'features',
            'erp',
            'last_coordinated',
            'last_updated',
            'coverage_notes'
        ]

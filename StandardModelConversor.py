#· Estandar Model 
indexsubelements = {"Up": 0, "Charm": 1, "Top": 2, "Down": 3, "Strange": 4,
    "Bottom": 5, "Antiup": 6, "Anticharm": 7, "Antitop": 8, "Antidown": 9,
    "Antistrange": 10, "Antibottom": 11, "Electron": 12, "Muon": 13, "Tau": 14,
    "Electronneutrino": 15, "Muonneutrino": 16, "Tauneutrino": 17, "Positron": 18,
    "Antimuon": 19, "Antitau": 20, "Electronantineutrino": 21, "Muonantineutrino": 22,
    "Tauantineutrino": 23, "Gluon": 24, "Photon": 25, "BosonZ": 26, "BosonWplus": 27,
    "BosonWless": 28, "Graviton": 29, "Higgs": 30}
     
subelements = [
    # Quarks
    {'Name': 'Up', 'mass MeVC2' : 2.3 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000000", 'Color name' : '\033[92mUp\033[0m', 'Color_binary' : '\033[92m00000000\033[0m'},
    {'Name': 'Charm', 'mass GeVC2' : 1.28 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000001", 'Color name' : '\033[92mCharm\033[0m', 'Color_binary' : '\033[92m00000001\033[0m'},
    {'Name': 'Top', 'mass GeVC2' : 173.1 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000010", 'Color name' : '\033[92mTop\033[0m', 'Color_binary' : '\033[92m00000010\033[0m'},
    {'Name': 'Down', 'mass MeVC2' : 4.8 , 'charge' : -1/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000011", 'Color name' : '\033[92mDown\033[0m', 'Color_binary' : '\033[92m00000011\033[0m'},
    {'Name': 'Strange', 'mass MeVC2' : 96 , 'charge' : -1/3 , 'spin' : 1/2 , 'Binary': "00000100", 'Color name' : '\033[92mStrange\033[0m', 'Color_binary' : '\033[92m00000100\033[0m'},
    {'Name': 'Bottom', 'mass GeVC2' : 4.18 , 'charge' : -1/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000101", 'Color name' : '\033[92mBottom\033[0m', 'Color_binary' : '\033[92m00000101\033[0m'},
    # Antiquarks
    {'Name': 'Antiup', 'mass MeVC2' : 2.3 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00000110", 'Color name' : '\033[94mAntiup\033[0m', 'Color_binary' : '\033[94m00000110\033[0m'},
    {'Name': 'Anticharm', 'mass GeVC2' : 1.28 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00000111", 'Color name' : '\033[94mAnticharm\033[0m', 'Color_binary' : '\033[94m00000111\033[0m'},
    {'Name': 'Antitop', 'mass GeVC2' : 173.1 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001000", 'Color name' : '\033[94mAntitop\033[0m', 'Color_binary' : '\033[94m00001000\033[0m'},
    {'Name': 'Antidown', 'mass MeVC2' : 4.8 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001001", 'Color name' : '\033[94mAntidown\033[0m', 'Color_binary' : '\033[94m00001001\033[0m'},
    {'Name': 'Antistrange', 'mass MeVC2' : 96 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001010", 'Color name' : '\033[94mAntistrange\033[0m', 'Color_binary' : '\033[94m00001010\033[0m'},
    {'Name': 'Antibottom', 'mass GeVC2' : 4.18 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001011", 'Color name' : '\033[94mAntibottom\033[0m', 'Color_binary' : '\033[94m00001011\033[0m'},
    # Leptons
    {'Name': 'Electron', 'mass MeVC2' : 0.511 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001100", 'Color name' : '\033[95mElectron\033[0m', 'Color_binary' : '\033[95m00001100\033[0m'},
    {'Name': 'Muon', 'mass MeVC2' : 105.7 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001101", 'Color name' : '\033[95mMuon\033[0m', 'Color_binary' : '\033[95m00001101\033[0m'},
    {'Name': 'Tau', 'mass GeVC2' : 1.7768 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001110", 'Color name' : '\033[95mTau\033[0m', 'Color_binary' : '\033[95m00001110\033[0m'},
    {'Name': 'Electronneutrino', 'mass eVC2' : 2.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001111", 'Color name' : '\033[95mElectronneutrino\033[0m', 'Color_binary' : '\033[95m00001111\033[0m'},
    {'Name': 'Muonneutrino', 'mass MeVC2' : 0.17 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00010000", 'Color name' : '\033[95mMuonneutrino\033[0m', 'Color_binary' : '\033[95m00010000\033[0m'},
    {'Name': 'Tauneutrino', 'mass MeVC2' : 18.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00010001", 'Color name' : '\033[95mTauneutrino\033[0m', 'Color_binary' : '\033[95m00010001\033[0m'},
    # Antileptons
    {'Name': 'Positron', 'mass MeVC2' : 0.511 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010010", 'Color name' : '\033[96mPositron\033[0m', 'Color_binary' : '\033[96m00010010\033[0m'},
    {'Name': 'Antimuon', 'mass MeVC2' : 105.7 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010011", 'Color name' : '\033[96mAntimuon\033[0m', 'Color_binary' : '\033[96m00010011\033[0m'},
    {'Name': 'Antitau', 'mass GeVC2' : 1.7768 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010100", 'Color name' : '\033[96mAntitau\033[0m', 'Color_binary' : '\033[96m00010100\033[0m'},
    {'Name': 'Electronantineutrino', 'mass eVC2' : 2.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010101", 'Color name' : '\033[96mElectronantineutrino\033[0m', 'Color_binary' : '\033[96m00010101\033[0m'},
    {'Name': 'Muonantineutrino', 'mass MeVC2' : 0.17 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010110", 'Color name' : '\033[96mMuonantineutrino\033[0m', 'Color_binary' : '\033[96m00010110\033[0m'},
    {'Name': 'Tauantineutrino', 'mass MeVC2' : 18.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010111", 'Color name' : '\033[96mTauantineutrino\033[0m', 'Color_binary' : '\033[96m00010111\033[0m'},
    # Gauge Bosons
    {'Name': 'Gluon', 'mass MeVC2' : 0 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011000", 'Color name' : '\033[101mGluon\033[0m', 'Color_binary' : '\033[101m00011000\033[0m'},
    {'Name': 'Photon', 'mass MeVC2' : 0 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011001", 'Color name' : '\033[101mPhoton\033[0m', 'Color_binary' : '\033[101m00011001\033[0m'},
    {'Name': 'BosonZ', 'mass GeVC2' : 91.2 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011010", 'Color name' : '\033[101mBosonZ\033[0m', 'Color_binary' : '\033[101m00011010\033[0m'},
    {'Name': 'BosonWplus', 'mass GeVC2' : 80.4 , 'charge' : 1 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011011", 'Color name' : '\033[101mBosonWplus\033[0m', 'Color_binary' : '\033[101m00011011\033[0m'},
    {'Name': 'BosonWless', 'mass GeVC2' : 80.4 , 'charge' : -1 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011100", 'Color name' : '\033[101mBosonWless\033[0m', 'Color_binary' : '\033[101m00011100\033[0m'},
    {'Name': 'Graviton', 'mass GeVC2' : 0 , 'charge' : 0 , 'spin' : 0 , 'Family' : 'Gauge Boson', 'Binary': "00011101", 'Color name' : '\033[101mGraviton\033[0m', 'Color_binary' : '\033[101m00011101\033[0m'},
    # Scalar Bosons
    {'Name': 'Higgs', 'mass GeVC2' : 126 , 'charge' : 0 , 'spin' : 0 , 'Family' : 'Scalar Boson', 'Binary': "00011110", 'Color name' : '\033[102mHiggs\033[0m', 'Color_binary' : '\033[102m00011110\033[0m'},]

# Quarks
Up = indexsubelements['Up']
Charm = indexsubelements['Charm']
Top = indexsubelements['Top']
Down = indexsubelements['Down']
Strange = indexsubelements['Strange']
Bottom = indexsubelements['Bottom']
# Antiquarks
Antiup = indexsubelements['Antiup']
Anticharm = indexsubelements['Anticharm']
Antitop = indexsubelements['Antitop']
Antidown = indexsubelements['Antidown']
Antistrange = indexsubelements['Antistrange']
Antibottom = indexsubelements['Antibottom']
# Leptons
Electron = indexsubelements['Electron']
Muon = indexsubelements['Muon']
Tau = indexsubelements['Tau']
Electronneutrino = indexsubelements['Electronneutrino']
Muonneutrino = indexsubelements['Muonneutrino']
Tauneutrino = indexsubelements['Tauneutrino']
# Antileptons
Positron = indexsubelements['Electron']
Antimuon = indexsubelements['Muon']
Antitau = indexsubelements['Tau']
Electronantineutrino = indexsubelements['Electronneutrino']
Muonantineutrino = indexsubelements['Muonneutrino']
Tauantineutrino = indexsubelements['Tauantineutrino']
# Gauge Bosons
Gluon = indexsubelements['Gluon']
Photon = indexsubelements['Photon']
BosonZ = indexsubelements['BosonZ']
BosonWplus = indexsubelements['BosonWplus']
BosonWless = indexsubelements['BosonWless']
Graviton = indexsubelements['Graviton']
# Scalar Bosons
Higgs = indexsubelements['Higgs']

# 1 GeV = 1.000.000.000 eV
# 1 MeV = 1.000.000 eV
# 1 eV = 0.000000000000000000160217733 J or 0.0000000000000000001602176565 J
# 1 J = 0.00000000000000001112650056 Kg
# Speed of light in a vacuum = 299.792.458 m/s

GeV = 1000000000 #eV
MeV = 1000000 #eV
eV = 0.000000000000000000160217733 #J
J = 0.00000000000000001112650056 #Kg

c_square = 299792458 ** 2

# Quarks
print("\nUp:\n")
print("Mass MeV/c² :", subelements[Up]['mass MeVC2'])
eV_divided_c_square_Up = subelements[Up]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Up)
J_divided_c_square_Up = eV_divided_c_square_Up * eV
print("Mass J/c² :", J_divided_c_square_Up)
Kg_divided_c_square_Up = J_divided_c_square_Up * J
print("Mass Kg/c² :", Kg_divided_c_square_Up)
Kg_Up = Kg_divided_c_square_Up / c_square
print("Mass Kg :", Kg_Up)

print("\nCharm:\n")
print("Mass GeV/c² :", subelements[Charm]['mass GeVC2'])
eV_divided_c_square_Charm = subelements[Charm]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Charm)
J_divided_c_square_Charm = eV_divided_c_square_Charm * eV
print("Mass J/c² :", J_divided_c_square_Charm)
Kg_divided_c_square_Charm = J_divided_c_square_Charm * J
print("Mass Kg/c² :", Kg_divided_c_square_Charm)
Kg_Charm = Kg_divided_c_square_Charm / c_square
print("Mass Kg :", Kg_Charm)

print("\nTop:\n")
print("Mass GeV/c² :", subelements[Top]['mass GeVC2'])
eV_divided_c_square_Top = subelements[Top]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Top)
J_divided_c_square_Top = eV_divided_c_square_Top * eV
print("Mass J/c² :", J_divided_c_square_Top)
Kg_divided_c_square_Top = J_divided_c_square_Top * J
print("Mass Kg/c² :", Kg_divided_c_square_Top)
Kg_Top = Kg_divided_c_square_Top / c_square
print("Mass Kg :", Kg_Top)

print("\nDown:\n")
print("Mass MeV/c² :", subelements[Down]['mass MeVC2'])
eV_divided_c_square_Down = subelements[Down]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Down)
J_divided_c_square_Down = eV_divided_c_square_Down * eV
print("Mass J/c² :", J_divided_c_square_Down)
Kg_divided_c_square_Down = J_divided_c_square_Down * J
print("Mass Kg/c² :", Kg_divided_c_square_Down)
Kg_Down = Kg_divided_c_square_Down / c_square
print("Mass Kg/c² :", Kg_Down)

print("\nStrange:\n")
print("Mass MeV/c² :", subelements[Strange]['mass MeVC2'])
eV_divided_c_square_Strange = subelements[Strange]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Strange)
J_divided_c_square_Strange = eV_divided_c_square_Strange * eV
print("Mass J/c² :", J_divided_c_square_Strange)
Kg_divided_c_square_Strange = J_divided_c_square_Strange * J
print("Mass Kg/c² :", Kg_divided_c_square_Strange)
Kg_Strange = Kg_divided_c_square_Strange / c_square
print("Mass Kg :", Kg_Strange)

print("\nBottom:\n")
print("Mass GeV/c² :", subelements[Bottom]['mass GeVC2'])
eV_divided_c_square_Bottom = subelements[Bottom]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Bottom)
J_divided_c_square_Bottom = eV_divided_c_square_Bottom * eV
print("Mass J/c² :", J_divided_c_square_Bottom)
Kg_divided_c_square_Bottom = J_divided_c_square_Bottom * J
print("Mass Kg/c² :", Kg_divided_c_square_Bottom)
Kg_Bottom = Kg_divided_c_square_Bottom / c_square
print("Mass Kg :", Kg_Bottom)

# Antiquarks
print("\nAntiup:\n")
print("Mass MeV/c² :", subelements[Antiup]['mass MeVC2'])
eV_divided_c_square_Antiup = subelements[Antiup]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Antiup)
J_divided_c_square_Antiup = eV_divided_c_square_Antiup * eV
print("Mass J/c² :", J_divided_c_square_Antiup)
Kg_divided_c_square_Antiup = J_divided_c_square_Antiup * J
print("Mass Kg/c² :", Kg_divided_c_square_Antiup)
Kg_Antiup = Kg_divided_c_square_Antiup / c_square
print("Mass Kg :", Kg_Antiup)

print("\nAnticharm:\n")
print("Mass GeV/c² :", subelements[Anticharm]['mass GeVC2'])
eV_divided_c_square_Anticharm = subelements[Anticharm]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Anticharm)
J_divided_c_square_Anticharm = eV_divided_c_square_Anticharm * eV
print("Mass J/c² :", J_divided_c_square_Anticharm)
Kg_divided_c_square_Anticharm = J_divided_c_square_Anticharm * J
print("Mass Kg/c² :", Kg_divided_c_square_Anticharm)
Kg_Anticharm = Kg_divided_c_square_Anticharm / c_square
print("Mass Kg :", Kg_Anticharm)

print("\nAntitop:\n")
print("Mass GeV/c² :", subelements[Antitop]['mass GeVC2'])
eV_divided_c_square_Antitop = subelements[Antitop]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Antitop)
J_divided_c_square_Antitop = eV_divided_c_square_Antitop * eV
print("Mass J/c² :", J_divided_c_square_Antitop)
Kg_divided_c_square_Antitop = J_divided_c_square_Antitop * J
print("Mass Kg/c² :", Kg_divided_c_square_Antitop)
Kg_Antitop = Kg_divided_c_square_Antitop / c_square
print("Mass Kg :", Kg_Antitop)

print("\nAntidown:\n")
print("Mass MeV/c² :", subelements[Antidown]['mass MeVC2'])
eV_divided_c_square_Antidown = subelements[Antidown]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Antidown)
J_divided_c_square_Antidown = eV_divided_c_square_Antidown * eV
print("Mass J/c² :", J_divided_c_square_Antidown)
Kg_divided_c_square_Antidown = J_divided_c_square_Antidown * J
print("Mass Kg/c² :", Kg_divided_c_square_Antidown)
Kg_Antidown = Kg_divided_c_square_Antidown / c_square
print("Mass Kg :", Kg_Antidown)

print("\nAntistrange:\n")
print("Mass MeV/c² :", subelements[Antistrange]['mass MeVC2'])
eV_divided_c_square_Antistrange = subelements[Antistrange]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Antistrange)
J_divided_c_square_Antistrange = eV_divided_c_square_Antistrange * eV
print("Mass J/c² :", J_divided_c_square_Antistrange)
Kg_divided_c_square_Antistrange = J_divided_c_square_Antistrange * J
print("Mass Kg/c² :", Kg_divided_c_square_Antistrange)
Kg_Antistrange = Kg_divided_c_square_Antistrange / c_square
print("Mass Kg :", Kg_Antistrange)

print("\nAntibottom:\n")
print("Mass GeV/c² :", subelements[Antibottom]['mass GeVC2'])
eV_divided_c_square_Antibottom = subelements[Antibottom]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Antibottom)
J_divided_c_square_Antibottom = eV_divided_c_square_Antibottom * eV
print("Mass J/c² :", J_divided_c_square_Antibottom)
Kg_divided_c_square_Antibottom = J_divided_c_square_Antibottom * J
print("Mass Kg/c² :", Kg_divided_c_square_Antibottom)
Kg_Antibottom = Kg_divided_c_square_Antibottom / c_square
print("Mass Kg :", Kg_Antibottom)

# Leptons
print("\nElectron:\n")
print("Mass MeV/c² :", subelements[Electron]['mass MeVC2'])
eV_divided_c_square_Electron = subelements[Electron]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Electron)
J_divided_c_square_Electron = eV_divided_c_square_Electron * eV
print("Mass J/c² :", J_divided_c_square_Electron)
Kg_divided_c_square_Electron = J_divided_c_square_Electron * J
print("Mass Kg/c² :", Kg_divided_c_square_Electron)
Kg_Electron = Kg_divided_c_square_Electron / c_square
print("Mass Kg :", Kg_Electron)

print("\nMuon:\n")
print("Mass MeV/c² :", subelements[Muon]['mass MeVC2'])
eV_divided_c_square_Muon = subelements[Muon]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Muon)
J_divided_c_square_Muon = eV_divided_c_square_Muon * eV
print("Mass J/c² :", J_divided_c_square_Muon)
Kg_divided_c_square_Muon = J_divided_c_square_Muon * J
print("Mass Kg/c² :", Kg_divided_c_square_Muon)
Kg_Muon = Kg_divided_c_square_Muon / c_square
print("Mass Kg :", Kg_Muon)

print("\nTau:\n")
print("Mass GeV/c² :", subelements[Tau]['mass GeVC2'])
eV_divided_c_square_Tau = subelements[Tau]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Tau)
J_divided_c_square_Tau = eV_divided_c_square_Tau * eV
print("Mass J/c² :", J_divided_c_square_Tau)
Kg_divided_c_square_Tau = J_divided_c_square_Tau * J
print("Mass Kg/c² :", Kg_divided_c_square_Tau)
Kg_Tau = Kg_divided_c_square_Tau / c_square
print("Mass Kg :", Kg_Tau)

print("\nElectronneutrino:\n")
print("Mass eV/c² :", subelements[Electronneutrino]['mass eVC2'])
eV_divided_c_square_Electronneutrino = subelements[Electronneutrino]['mass eVC2']
print("Mass eV/c² :", eV_divided_c_square_Electronneutrino)
J_divided_c_square_Electronneutrino = eV_divided_c_square_Electronneutrino * eV
print("Mass J/c² :", J_divided_c_square_Electronneutrino)
Kg_divided_c_square_Electronneutrino = J_divided_c_square_Electronneutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Electronneutrino)
Kg_Electronneutrino = Kg_divided_c_square_Electronneutrino / c_square
print("Mass Kg :", Kg_Electronneutrino)

print("\nMuonneutrino:\n")
print("Mass MeV/c² :", subelements[Muonneutrino]['mass MeVC2'])
eV_divided_c_square_Muonneutrino = subelements[Muonneutrino]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Muonneutrino)
J_divided_c_square_Muonneutrino = eV_divided_c_square_Muonneutrino * eV
print("Mass J/c² :", J_divided_c_square_Muonneutrino)
Kg_divided_c_square_Muonneutrino = J_divided_c_square_Muonneutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Muonneutrino)
Kg_Muonneutrino = Kg_divided_c_square_Muonneutrino / c_square
print("Mass Kg :", Kg_Muonneutrino)

print("\nTauneutrino:\n")
print("Mass MeV/c² :", subelements[Tauneutrino]['mass MeVC2'])
eV_divided_c_square_Tauneutrino = subelements[Tauneutrino]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Tauneutrino)
J_divided_c_square_Tauneutrino = eV_divided_c_square_Tauneutrino * eV
print("Mass J/c² :", J_divided_c_square_Tauneutrino)
Kg_divided_c_square_Tauneutrino = J_divided_c_square_Tauneutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Tauneutrino)
Kg_Tauneutrino = Kg_divided_c_square_Tauneutrino / c_square
print("Mass Kg :", Kg_Tauneutrino)

# Antileptons
print("\nPositron:\n")
print("Mass MeV/c² :", subelements[Positron]['mass MeVC2'])
eV_divided_c_square_Positron = subelements[Positron]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Positron)
J_divided_c_square_Positron = eV_divided_c_square_Positron * eV
print("Mass J/c² :", J_divided_c_square_Positron)
Kg_divided_c_square_Positron = J_divided_c_square_Positron * J
print("Mass Kg/c² :", Kg_divided_c_square_Positron)
Kg_Positron = Kg_divided_c_square_Positron / c_square
print("Mass Kg :", Kg_Positron)

print("\nAntimuon:\n")
print("Mass MeV/c² :", subelements[Antimuon]['mass MeVC2'])
eV_divided_c_square_Antimuon = subelements[Antimuon]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Antimuon)
J_divided_c_square_Antimuon = eV_divided_c_square_Antimuon * eV
print("Mass J/c² :", J_divided_c_square_Antimuon)
Kg_divided_c_square_Antimuon = J_divided_c_square_Antimuon * J
print("Mass Kg/c² :", Kg_divided_c_square_Antimuon)
Kg_Antimuon = Kg_divided_c_square_Antimuon / c_square
print("Mass Kg :", Kg_Antimuon)

print("\nAntitau:\n")
print("Mass GeV/c² :", subelements[Antitau]['mass GeVC2'])
eV_divided_c_square_Antitau = subelements[Antitau]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Antitau)
J_divided_c_square_Antitau = eV_divided_c_square_Antitau * eV
print("Mass J/c² :", J_divided_c_square_Antitau)
Kg_divided_c_square_Antitau = J_divided_c_square_Antitau * J
print("Mass Kg/c² :", Kg_divided_c_square_Antitau)
Kg_Antitau = Kg_divided_c_square_Antitau / c_square
print("Mass Kg :", Kg_Antitau)

print("\nElectronantineutrino:\n")
print("Mass eV/c² :", subelements[Electronantineutrino]['mass eVC2'])
eV_divided_c_square_Electronantineutrino = subelements[Electronantineutrino]['mass eVC2'] / MeV
print("Mass eV/c² :", eV_divided_c_square_Electronantineutrino)
J_divided_c_square_Electronantineutrino = eV_divided_c_square_Electronantineutrino * eV
print("Mass J/c² :", J_divided_c_square_Electronantineutrino)
Kg_divided_c_square_Electronantineutrino = J_divided_c_square_Electronantineutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Electronantineutrino)
Kg_Electronantineutrino = Kg_divided_c_square_Electronantineutrino / c_square
print("Mass Kg :", Kg_Electronantineutrino)

print("\nMuonantineutrino:\n")
print("Mass MeV/c² :", subelements[Muonantineutrino]['mass MeVC2'])
eV_divided_c_square_Muonantineutrino = subelements[Muonantineutrino]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Muonantineutrino)
J_divided_c_square_Muonantineutrino = eV_divided_c_square_Muonantineutrino * eV
print("Mass J/c² :", J_divided_c_square_Muonantineutrino)
Kg_divided_c_square_Muonantineutrino = J_divided_c_square_Muonantineutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Muonantineutrino)
Kg_Muonantineutrino = Kg_divided_c_square_Muonantineutrino / c_square
print("Mass Kg :", Kg_Muonantineutrino)

print("\nTauantineutrino:\n")
print("Mass MeV/c² :", subelements[Tauantineutrino]['mass MeVC2'])
eV_divided_c_square_Tauantineutrino = subelements[Tauantineutrino]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Tauantineutrino)
J_divided_c_square_Tauantineutrino = eV_divided_c_square_Tauantineutrino * eV
print("Mass J/c² :", J_divided_c_square_Tauantineutrino)
Kg_divided_c_square_Tauantineutrino = J_divided_c_square_Tauantineutrino * J
print("Mass Kg/c² :", Kg_divided_c_square_Tauantineutrino)
Kg_Tauantineutrino = Kg_divided_c_square_Tauantineutrino / c_square
print("Mass Kg :", Kg_Tauantineutrino)

# Gauge Bosons
print("\nGluon:\n")
print("Mass MeV/c² :", subelements[Gluon]['mass MeVC2'])
eV_divided_c_square_Gluon = subelements[Gluon]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Gluon)
J_divided_c_square_Gluon = eV_divided_c_square_Gluon * eV
print("Mass J/c² :", J_divided_c_square_Gluon)
Kg_divided_c_square_Gluon = J_divided_c_square_Gluon * J
print("Mass Kg/c² :", Kg_divided_c_square_Gluon)
Kg_Gluon = Kg_divided_c_square_Gluon / c_square
print("Mass Kg :", Kg_Gluon)

print("\nPhoton:\n")
print("Mass MeV/c² :", subelements[Photon]['mass MeVC2'])
eV_divided_c_square_Photon = subelements[Photon]['mass MeVC2'] * MeV
print("Mass eV/c² :", eV_divided_c_square_Photon)
J_divided_c_square_Photon = eV_divided_c_square_Photon * eV
print("Mass J/c² :", J_divided_c_square_Photon)
Kg_divided_c_square_Photon = J_divided_c_square_Photon * J
print("Mass Kg/c² :", Kg_divided_c_square_Photon)
Kg_Photon = Kg_divided_c_square_Photon / c_square
print("Mass Kg :", Kg_Photon)

print("\nBosonZ:\n")
print("Mass GeV/c² :", subelements[BosonZ]['mass GeVC2'])
eV_divided_c_square_BosonZ = subelements[BosonZ]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_BosonZ)
J_divided_c_square_BosonZ = eV_divided_c_square_BosonZ * eV
print("Mass J/c² :", J_divided_c_square_BosonZ)
Kg_divided_c_square_BosonZ = J_divided_c_square_BosonZ * J
print("Mass Kg/c² :", Kg_divided_c_square_BosonZ)
Kg_BosonZ = Kg_divided_c_square_BosonZ / c_square
print("Mass Kg :", Kg_BosonZ)

print("\nBosonWplus:\n")
print("Mass GeV/c² :", subelements[BosonWplus]['mass GeVC2'])
eV_divided_c_square_BosonWplus = subelements[BosonWplus]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_BosonWplus)
J_divided_c_square_BosonWplus = eV_divided_c_square_BosonWplus * eV
print("Mass J/c² :", J_divided_c_square_BosonWplus)
Kg_divided_c_square_BosonWplus = J_divided_c_square_BosonWplus * J
print("Mass Kg/c² :", Kg_divided_c_square_BosonWplus)
Kg_BosonWplus = Kg_divided_c_square_BosonWplus / c_square
print("Mass Kg :", Kg_BosonWplus)

print("\nBosonWless:\n")
print("Mass GeV/c² :", subelements[BosonWless]['mass GeVC2'])
eV_divided_c_square_BosonWless = subelements[BosonWless]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_BosonWless)
J_divided_c_square_BosonWless = eV_divided_c_square_BosonWless * eV
print("Mass J/c² :", J_divided_c_square_BosonWless)
Kg_divided_c_square_BosonWless = J_divided_c_square_BosonWless * J
print("Mass Kg/c² :", Kg_divided_c_square_BosonWless)
Kg_BosonWless = Kg_divided_c_square_BosonWless / c_square
print("Mass Kg :", Kg_BosonWless)

print("\nGraviton:\n")
print("Mass GeV/c² :", subelements[Graviton]['mass GeVC2'])
eV_divided_c_square_Graviton = subelements[Graviton]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Graviton)
J_divided_c_square_Graviton = eV_divided_c_square_Graviton * eV
print("Mass J/c² :", J_divided_c_square_Graviton)
Kg_divided_c_square_Graviton = J_divided_c_square_Graviton * J
print("Mass Kg/c² :", Kg_divided_c_square_Graviton)
Kg_Graviton = Kg_divided_c_square_Graviton / c_square
print("Mass Kg :", Kg_Graviton)

# Scalar Bosons
print("\nHiggs:\n")
print("Mass GeV/c² :", subelements[Higgs]['mass GeVC2'])
eV_divided_c_square_Higgs = subelements[Higgs]['mass GeVC2'] * GeV
print("Mass eV/c² :", eV_divided_c_square_Higgs)
J_divided_c_square_Higgs = eV_divided_c_square_Higgs * eV
print("Mass J/c² :", J_divided_c_square_Higgs)
Kg_divided_c_square_Higgs = J_divided_c_square_Higgs * J
print("Mass Kg/c² :", Kg_divided_c_square_Higgs)
Kg_Higgs = Kg_divided_c_square_Higgs / c_square
print("Mass Kg :", Kg_Higgs)

# A!ÜSKA

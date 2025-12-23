# Write a program where in following text will replace North Macedonia with Macedonia without allowing any extra spaces:
# “North Macedonia is a member of NATO, the Council of Europe, the World Bank, OSCE, CEFTA, BSEC and the WTO. Since 2005, it has also been a candidate for joining the European Union. North Macedonia is an upper-middle-income country by the World Bank's definitions and has undergone considerable economic reform since its independence in developing an open economy. It is a developing country with a very high Human Development Index and low income inequality; and provides social security, a universal health care system, and free primary and secondary education to its citizens.”

NMK="North Macedonia is a member of NATO, the Council of Europe, the World Bank, OSCE, CEFTA, BSEC and the WTO. Since 2005, it has also been a candidate for joining the European Union. North Macedonia is an upper-middle-income country by the World Bank's definitions and has undergone considerable economic reform since its independence in developing an open economy. It is a developing country with a very high Human Development Index and low income inequality; and provides social security, a universal health care system, and free primary and secondary education to its citizens."

MK=NMK.replace("North Macedonia", "Macedonia")

print(MK)
import random

data = [
    ["NightFury_87", "K9#mP2$xL5@vR"], ["ShadowHunter", "qW3#eR5$tY7&uI8"],
    ["PhantomX_22", "zXc9!vBn4*mKl2"], ["DarkSoul_99", "P@ssw0rd2024!"],
    ["IceDragon_45", "F!r3Dr@g0nX9"], ["StormBringer", "S7orm#B8ring$er"],
    ["NightRaven_12", "R@v3n$D@rkN1ght"], ["SilverWolf_56", "W0lfP@ck#Silver"],
    ["GoldenEagle_78", "E@g1e$G0lden123"], ["RedPhoenix_34", "Ph0en!x#F1reR3d"],
    ["BlueTiger_90", "T!g3r$Blu3Str1pe"], ["BlackWidow_67", "W!d0w$B1ackSp!der"],
    ["WhiteGhost_23", "Gh0st$Wh1teShad0w"], ["GreenViper_11", "V!p3r$Gr33nFang"],
    ["CrimsonKing_55", "K!ng$Cr!ms0nRul3"], ["IronFist_44", "F!st$!r0nPunchX9"],
    ["SteelHeart_77", "H3art$St33lS0ul"], ["ThunderGod_88", "G0d$Thund3rB0lt"],
    ["FrostGiant_33", "G!4nt$Fr0st1ceX"], ["FlameLord_66", "L0rd$Fl4m3F!re"],
    ["VoidWalker_99", "W4lk3r$V0!dShad0w"], ["StarGlider_22", "Gl!d3r$St4rL!ght"],
    ["MoonHunter_44", "Hunt3r$M00nBeamX"], ["SunKnight_11", "Kn!ght$SunR4y3"],
    ["SkyCaptain_77", "C4pt4!n$SkyH!gh"], ["OceanMaster_55", "M4st3r$Oc34nD33p"],
    ["FireWizard_33", "W!z4rd$F!r3Sp!ke"], ["EarthShaker_88", "Sh4k3r$E4rthQu4ke"],
    ["WindRunner_66", "Runn3r$W!ndSt0rm"], ["LightBringer_22", "Br!ng3r$L!ghtD4wn"],
    ["DoomSlayer_99", "Sl4y3r$D00mH3ll"], ["RageBeast_44", "B34st$R4g3F!st"],
    ["SilentKill_77", "K!ll3r$S!l3ntD3ath"], ["SwiftArrow_11", "Arr0w$Sw!ftStr1ke"],
    ["BraveHeart_33", "H3art$Br4v3S0ulX"], ["DarkBlade_55", "Bl4d3$D4rkN!ght"],
    ["LightSpear_88", "Sp34r$L!ghtStr!ke"], ["HolyShield_66", "Sh!3ld$H0lyKn!ght"],
    ["EvilEye_22", "Ev!l$Ey3S0ulR34p"], ["MagicHand_44", "M4g!c$H4ndTr!ck"],
    ["QuickSilver_77", "Qu!ck$S!lv3rRunn"], ["IronWill_99", "W!ll$!r0nM!ndX9"],
    ["SteelSoul_11", "S0ul$St33lH3art"], ["CopperMind_33", "M!nd$C0pp3rW!re"],
    ["BronzeFist_55", "F!st$Br0nz3Knuck"], ["TitanCore_66", "C0r3$T!t4nP0w3r"],
    ["AtlasPrime_22", "Pr!m3$4tl4sStr0ng"], ["OmegaZero_44", "Z3r0$0m3g4F!n4l"],
    ["AlphaOne_77", "0n3$4lph4F!rstX"], ["BetaTwo_88", "Tw0$B3t4S3c0nd"],
    ["GammaRay_99", "R4y$G4mm4R4d!4t"], ["DeltaForce_11", "F0rc3$D3lt4Str!k3"],
    ["SigmaSix_33", "S!x$S!gm4C0d3X9"], ["NeonGhost_55", "Gh0st$N30nL!ght"],
    ["CyberPunk_66", "Punk$Cyb3rN0!r"], ["NetRunner_22", "Runn3r$N3tW!r3"],
    ["DataLord_44", "L0rd$D4t4Str34m"], ["CodeBreaker_77", "Br34k3r$C0d3R3d"],
    ["ZeroCool_88", "C00l$Z3r0H4ck"], ["AcidBurn_99", "Burn$4c!dFl4m3s"],
    ["CrashOverride_11", "0v3rr!d3$Cr4shX9"], ["PhantomLord_33", "L0rd$Ph4nt0mSh4d0w"],
    ["ShadowMage_55", "M4g3$Sh4d0wC4st"], ["DarkPriest_66", "Pr!3st$D4rkW0rship"],
    ["LightCleric_22", "Cl3r!c$L!ghtH34l"], ["StormWizard_44", "W!z4rd$St0rmC4st"],
    ["FrostMage_77", "M4g3$Fr0stB!t3"], ["FirePriest_88", "Pr!3st$F!r3H34l"],
    ["EarthWarden_99", "W4rd3n$E4rthSh!3ld"], ["AirRider_11", "R!d3r$4!rW1nd"],
    ["WaterWalker_33", "W4lk3r$W4t3rFl0w"], ["NatureSpirit_55", "Sp!r!t$N4tur3Gr0w"],
    ["BeastMaster_66", "M4st3r$B34stC4ll"], ["HunterKing_22", "K!ng$Hunt3rTr4ck"],
    ["WarriorQueen_44", "Qu33n$W4rr!0rBl00d"], ["PaladinLord_77", "L0rd$P4l4d!nSh!3ld"],
    ["RogueShadow_88", "Sh4d0w$R0gu3Kn!f3"], ["ArcherStar_99", "St4r$4rch3rB0w"],
    ["BerserkerRage_11", "R4g3$B3rs3rk3rF!st"], ["VikingKing_33", "K!ng$V!k!ngH0rn"],
    ["SamuraiBlade_55", "Bl4d3$S4mur4!K4t4n4"], ["NinjaShadow_66", "Sh4d0w$N!nj4St34lth"],
    ["RoninWolf_22", "W0lf$R0n!nL0n3"], ["DragonSoul_44", "S0ul$Dr4g0nF!r3"],
    ["TigerClaw_77", "Cl4w$T!g3rStr!p3"], ["PhoenixWing_88", "W!ng$Ph03n!xF!r3"],
    ["DragonHeart_99", "H34rt$Dr4g0nSc4l3"], ["WolfPack_11", "P4ck$W0lfByt3"],
    ["EagleEye_33", "Ey3$E4gl3V!s!0n"], ["HawkVision_55", "V!s!0n$H4wkStr!k3"],
    ["FalconPunch_66", "Punch$F4lc0nF!st"], ["RavenBeak_22", "B34k$R4v3nD4rk"],
    ["CrowFeather_44", "F34th3r$Cr0wBl4ck"], ["OwlWisdom_77", "W!sd0m$0wlKn0wl"],
    ["BatWing_88", "W!ng$B4tN!ght"], ["SpiderSilk_99", "S!lk$Sp!d3rW3b"],
    ["ScorpionTail_11", "T4!l$Sc0rp!0nSt!ng"], ["SnakeFang_33", "F4ng$Sn4k3V3nom"]
]

acc = random.choice(data)

print("----------------------------")
print(f"LOGIN: {acc[0]}")
print(f"PASSWORD: {acc[1]}")
print("----------------------------")

input("Press Enter to exit...")

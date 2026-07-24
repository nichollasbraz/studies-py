def vogais():
    vogaisTab = (
        'fazer','brincar','chorar','viver','amar',
        'gustavo','leonardo','moisés','messias','micael',
        'paralelepipedo','cilindro','cubo','losango','pentagono',
        'pizza','churros','alcatra','pudim','sorvete'
        )

    for i in vogaisTab:
        print(f"vogais de {i}:", end="")
        for l in i:
            if l.lower() in 'aeiou':
                print(f' {l}', end="" )
        print("\n")

vogais()

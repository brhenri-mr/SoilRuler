import ezdxf


def creatRuler(p_i, delta_passo, db):
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Linha inicial
    msp.add_line((-20, 0), (30, 0), dxfattribs={"layer": "MyLayer"})


    # Quantidade de camadas
    qdnt_camadas = db['tamanho'].sum()+1

    # Construindo a régua
    for i in range(qdnt_camadas):
        vertices = [(0, -100*i), (10, -100*i), (10, -100-100*i), (0, -100-i*100)]
        print(vertices)
        if i%2 ==0:
    
            msp.add_lwpolyline(vertices, close=True)


        else:
            hatch = msp.add_hatch(
                color=1,
                dxfattribs={
                    "hatch_style": ezdxf.const.HATCH_STYLE_NESTED,
                },
            )

            hatch.paths.add_polyline_path(
                vertices,
                is_closed=True,
                flags=ezdxf.const.BOUNDARY_PATH_EXTERNAL,
        )

    acumulo = p_i

    # Atribuindo os limites e os nomes
    for i in range(db.shape[0]):

        if i ==0:
            text_point = acumulo/2 + (1 - db['tamanho'][i])*(delta_passo)/2

            acumulo = acumulo + (1 - db['tamanho'][i])*(delta_passo)
            
        else:

            text_point = acumulo + (db['tamanho'][i])*(delta_passo)/2

            acumulo = acumulo + (db['tamanho'][i])*(delta_passo)

        msp.add_line((-20, acumulo), (30, acumulo), dxfattribs={"layer": "Limites"})

        msp.add_text(db['camada'][i], dxfattribs={'insert': (15, text_point), 'height': 5})


    doc.saveas("Regua.dxf")



if __name__ == '__main__':
    creatRuler(-1.45,)








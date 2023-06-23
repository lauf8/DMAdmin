import datetime
from django.shortcuts import render
import pandas as pd
from .models import MembroCastelo
from organizacao.models import Capitulo, Castelo

def read_excel_view_castelo(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')
        if excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                    id_demolay = row['ID']
                    print(id_demolay)
                    membro_novo  = MembroCastelo.objects.filter(id_demolay=id_demolay).first()
                    print(membro_novo)
                    if membro_novo is None:
                        nome_castelo =  row['NOME CASTELO']
                        castelo = Castelo.objects.filter(nome=nome_castelo).first()
                        if castelo:
                            membro = MembroCastelo()
                            membro.id_demolay = id_demolay
                            membro.nome = row['NOME']
                            data_iniciacao_us = row['INICIAÇÃO']
                            data_nascimento_us = row['NASCIMENTO']
                            data_iniciacao = datetime.datetime.strptime(data_iniciacao_us, '%d/%m/%Y').strftime('%Y-%m-%d')
                            data_nascimento = datetime.datetime.strptime(data_nascimento_us, '%d/%m/%Y').strftime('%Y-%m-%d')
                            membro.castelo = castelo
                            membro.iniciacao = data_iniciacao
                            membro.data_nascimento = data_nascimento
                            membro.save()
                            success_message = 'Os dados foram importados com sucesso.'
                            
                        else:
                            error_message = 'Por favor Verifique se o Castelo Já foi criado.'
                            return render(request, 'read_excel.html', {'error_message': error_message})
                            
                    else:
                        success_message = 'Os dados foram importados com sucesso, mas existem membros que ja foram cadastrados nessa planilha'
                        continue                        
                       
                            

                    
            
            return render(request, 'import_excel.html', {'success_message': success_message})
       
            
            
        else:
            error_message = 'Por favor, faça upload de um arquivo Excel válido (.xlsx).'
            return render(request, 'read_excel.html', {'error_message': error_message})
    return render(request, 'read_excel.html')

# unieuro-concorrente-202601-atividade3
Paralelizar avaliador de arquivos de log.

## Passo-a-passo

1) Implemente a solução paralela que possa ser executada com 2, 4, 8, 12 processos
2) Execute o experimento para medir os tempos em paralelo
3) Construa um relatório de análise dos resultados (MODELO DO RELATÓRIO RELATORIO_MODELO.MD - SALVAR COMO README.MD)
4) Crie um repositório público no GitHub incluindo os programas python e o README.MD no formato de relatório.
5) Responda o questionário no AVA

## Problema

Uma empresa precisa processar grandes volumes de arquivos texto contendo logs operacionais. Cada arquivo deve ser analisado para extrair informações relevantes que serão utilizadas em relatórios gerenciais.

Atualmente, o sistema realiza esse processamento de forma sequencial (serial), o que gera um tempo elevado de execução quando há muitos arquivos.

Para melhorar o desempenho, deseja-se evoluir o sistema para uma versão paralela, utilizando o modelo produtor-consumidor com buffer limitado.


## Exemplo1
No processamento da pasta log1 o resultado esperado é:

=== RESULTADO CONSOLIDADO ===  
Total de linhas: 600  
Total de palavras: 12000  
Total de caracteres: 82085  
  
Contagem de palavras-chave:  
  erro: 1993  
  warning: 1998  
  info: 1983  


## Dicas

1) Implemente a solução utilizando os arquivos da pasta log1.
2) Realize o experimento e construa o relatório utilizando os arquivos da pasta log2.

=== EXECUÇÃO SERIAL ===
Arquivos processados: 1000  
Tempo total: 115.9621 segundos  
  
=== RESULTADO CONSOLIDADO ===  
Total de linhas: 10000000  
Total de palavras: 200000000  
Total de caracteres: 1366663305  
  
Contagem de palavras-chave:  
  erro: 33332083  
  warning: 33330520  
  info: 33329065  
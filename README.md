# Serviço de manutenção de uma list (DBList) com gRPC
Implementação de um serviço de manipulação de uma lista (DBList), usando RPC e interfaces genéricas, por meio da biblioteca gRPC.

A pasta "protos" apresenta o arquivo "DBListService.proto" que específica a interface genérica do servico DBList construído. É determinado as interfaces e as mensagens trocadas entre o cliente e o servidor.

A pasta "python" apresenta os códigos em Python da implementação.

O arquivo "const.py" contém o IP e a porta do servidor.

O arquivo "server.py" é referente a definição das implementação dos métodos que operam sobre a lista.

O arquivo "client.py" é referente ao código que executa as chamadas (RPC) que operam sobre a lista existente no servidor.

A seguinte linha de código pode ser executada (dentro da pasta "python") para a compilação da interface genérica.
- python3 -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/DBListService.proto

# Vídeo da apresentação
-

Feature: Cadastro e Gerenciamento de Usuários
  Como administrador do sistema
  Eu quero poder gerenciar usuários
  Para que eu possa manter as informações de usuários atualizadas e remover usuários quando necessário

  Scenario Outline: Cadastro de um novo usuário com sucesso
    Given que não há usuários cadastrados
    When eu cadastro um usuário com nome "<name>" e email "<email>"
    Then o sistema deve registrar o usuário "<name>" com o email "<email>"
    And o sistema deve ter 1 usuário cadastrado
    And o sistema não deve retornar nenhum erro

    Examples:
      | name       | email                    |
      | Guilherme  | Guilherme@example.com    |
      | Andrieria  | Andrieria@example.com    |
      | Kelvin     | Kelvin@example.com       |
      | João Paulo | JoãoPaulo@example.com    |
      | Bruno      | Bruno@example.com        |

Scenario Outline: Tentativa de cadastro de um usuário com email já registrado
  Given que o usuário "<existing_name>" com email "<existing_email>" está cadastrado
  When eu cadastro um usuário com nome "<new_name>" e email "<existing_email>"
  Then o sistema deve retornar um erro dizendo que o email já está registrado

  Examples:
    | existing_name | existing_email        | new_name |
    | Maria         | maria@example.com     | Pedro    |
    | Ana           | ana@example.com       | João     |

  Scenario Outline: Atualização de informações do usuário
    Given que o usuário "<old_name>" com email "<old_email>" está cadastrado
    When eu atualizo o nome do usuário para "<new_name>" e o email para "<new_email>"
    Then o sistema deve atualizar o usuário para o nome "<new_name>" e o email "<new_email>"

    Examples:
      | old_name | old_email             | new_name | new_email              |
      | Maria    | maria@example.com     | Maria S. | maria.s@example.com    |
      | João     | joao@example.com      | João P.  | joao.p@example.com     |

  Scenario: Remoção de um usuário
    Given que o usuário "Ana" com email "ana@example.com" está cadastrado
    When eu removo o usuário com email "ana@example.com"
    Then o sistema não deve ter nenhum usuário com email "ana@example.com"

  Scenario: Tentativa de atualização de usuário inexistente
    Given que não há usuários com o email "naoexistente@example.com"
    When eu tento atualizar o usuário com o email "naoexistente@example.com"
    Then o sistema deve retornar um erro dizendo que o usuário não foi encontrado

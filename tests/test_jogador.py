from jogaodor import Jogador

def test_jogador(exercitos,carta_objetivo,cartas_territorio):
    jogador = Jogador(exercitos,carta_objetivo,cartas_territorio)
    assert isinstance(jogador,Jogador)
    

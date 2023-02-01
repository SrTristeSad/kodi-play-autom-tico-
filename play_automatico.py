import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

ADDON = xbmcaddon.Addon()

def play_video(video_url):
    """Função para iniciar a reprodução de um vídeo."""
    xbmc.Player().play(video_url)

def get_next_video(season, episode):
    """Função para obter o URL do próximo vídeo na temporada."""
    # Aqui você pode incluir o código para acessar sua coleção de vídeos
    # e retornar o URL do próximo vídeo na temporada
    return next_video_url

def on_playback_ended():
    """Função para ser chamada quando o vídeo atual terminar."""
    current_season = get_current_season()
    current_episode = get_current_episode()
    next_season = current_season
    next_episode = current_episode + 1
    next_video_url = get_next_video(next_season, next_episode)
    if not next_video_url:
        # Não há mais episódios nesta temporada
        # Perguntar ao usuário se ele deseja começar a próxima temporada
        next_season += 1
        next_episode = 1
        next_video_url = get_next_video(next_season, next_episode)
        if not next_video_url:
            xbmc.log("Não há mais vídeos disponíveis.")
            return
        # Mostrar diálogo para escolher a próxima temporada
        dialog = xbmcgui.Dialog()
        next_season_options = get_season_options()
        selected_index = dialog.select("Escolha a próxima temporada:", next_season_options)
        if selected_index == -1:
            # Usuário cancelou
            return
        next_season = get_season_from_option(next_season_options[selected_index])
        next_video_url = get_next_video(next_season, next_episode)
    play_video(next_video_url)

def run():
    """Função principal para iniciar a reprodução automática."""
    current_video_url = get_current_video_url()
    play_video(current_video_url)
    xbmc.Monitor().waitForAbort(onPlayBackEnded=on_playback_ended)

if __name__ == "__main__":
    run()

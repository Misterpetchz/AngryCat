       offset = 0
        count = 0
        sorted_name = sorted(player_score.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(sorted_name)
        name = list(sorted_dict.keys())

        subject = font.render('High Score', False, 'gold')
        subject_rect = subject.get_rect(center = ((1280 // 2), 100))
        pygame.draw.rect(display_surf, UI_BG_COLOR,subject_rect.inflate(20, 20))
        display_surf.blit(subject, subject_rect)

        for key in name:
            if count <= 4:
                image = pygame.image.load('../Assets/start_menu/screen.png')
                rect = image.get_rect(topleft = (0, 0))
                text_surf = font.render(key, False, 'gold')
                text_rect = text_surf.get_rect(topright = ((1280 // 2) - 100, 200 + offset))
                score_surf = font.render(str(int(sorted_dict[key])), False, 'gold')
                score_rect = score_surf.get_rect(topleft = ((1280 // 2) + 100, 200 + offset))
                
                offset += 100
                count += 1
                pygame.draw.rect(display_surf, UI_BG_COLOR, text_rect.inflate(20, 20))
                display_surf.blit(text_surf, text_rect)
                pygame.draw.rect(display_surf, UI_BG_COLOR, score_rect.inflate(20, 20))
                display_surf.blit(score_surf, score_rect)

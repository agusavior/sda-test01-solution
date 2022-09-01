
from typing import Set
from akabab import AkababAPI
from mycanvas import MyCanvas
from config import *


def main():
    # Fetch from API
    superheroes = AkababAPI.get_all()
    occupations = AkababAPI.get_all_occupations()

    # Take only the first 10
    superheroes = superheroes[0: NUMBER_OF_SUPERHEROES]

    # Create PDF canvas
    canvas = MyCanvas(OUT_FILENAME)
    
    # In order to not draw the same superhereo twice
    ploted_superherores_ids: Set[int] = set()

    for occupation in occupations:
        # Occupation title hasn't been drawn yet
        the_occupation_title_has_been_drawn = False

        for superheroe in superheroes:
            # If the superhero hasn't this occupation, continue
            if not superheroe.has_specific_occupation(occupation):
                continue

            # If the superhero is already ploted, continue
            if superheroe.id in ploted_superherores_ids:
                continue

            # Draw the occupation title only if needed
            if not the_occupation_title_has_been_drawn:
                canvas.plot_occupation_title(title=occupation)

                # Flag
                the_occupation_title_has_been_drawn = True
            
            # Plot
            canvas.plot_superheroe(superheroe)

            # Recall
            ploted_superherores_ids.add(superheroe.id)

    # Plot non categorized superheroes
    we_didnt_plot_every_one = len(ploted_superherores_ids) < len(superheroes)
    if we_didnt_plot_every_one:
        # Plot title
        canvas.plot_occupation_title(title='Undefined occupation')

        # Plot every superheroe that hasn't been ploted
        for superheroe in superheroes:
            if superheroe.id not in ploted_superherores_ids:
                # Debug print
                print('Warning. Uncategorized superheroe detected. Occupation description = ', superheroe.occupation_description)

                # Plot
                canvas.plot_superheroe(superheroe)

    # Plot and create file
    canvas.show_page_and_save()


# Main
if __name__ == '__main__':
    main()

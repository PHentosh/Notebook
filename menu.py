"""
Menu module
"""
import notebook

class Menu:
    """
    Notebook menu
    """

    def create_new_notebook(self):
        """
        Create new notebook
        """
        self.Notebook = notebook.Notebook()

    def work_with_notebook(self):
        """
        WOrk with notebook
        """
        list_of_commands = ['modify tags', 'modify memo', 'search by tag', 'create new note']
        command = ''
        while command != "exit":
            print('Here is what you can do:')
            for com in list_of_commands:
                print(com)
            print('to exit, print \"exit\"')
            command = input('Chose your command: ')
            if command == 'modify tags':
                note_id = input('pleas input your note id: ')
                tags = input('pleas input your tags(like: 1, 2, 3, 4): ')
                res = self.Notebook.modify_tags(note_id, tags)
                if res != None:
                    print(res + '\n')
                else:
                    print('Tags changed sucsesfuly\n')
            elif command == 'modify memo':
                note_id = input('pleas input your note id: ')
                memo = input('pleas input your memo: ')
                res = self.Notebook.modify_memo(note_id, memo)
                if res != None:
                    print(res +'\n')
                else:
                    print('Memo changed sucsesfuly\n')
            elif command == 'search by tag':
                tags = input('pleas input your tag: ')
                res = self.Notebook.search(tags)
                if res != []:
                    for i in res:
                        print(f'Id: {i[0]}, Memo:\n{i[1]}\n')
                else:
                    print('There is no results\n')
            elif command == 'create new note':
                memo = input('pleas input your memo: ')
                tags = input('pleas input your tags(like: 1, 2, 3, 4): ')
                self.Notebook.new_note(memo, tags)
                print('New note added\n')
            elif command == 'exit':
                pass
            else:
                print('Wrong command\n')


Men = Menu()

Men.create_new_notebook()
Men.work_with_notebook()
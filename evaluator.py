from solution import Solution
from objects import Contributor, Project
from typing import List, Set

class Evaluator:
    def __init__(self):
        pass
    
    def evaluator(self, solutions: Set[Solution], contributors:Set[Contributor], projects:Set[Project]):
        final_score = 0
        project_solutions = solutions.projectsolutions
        done_project = [0] * len(project_solution)
        for project_index, project_solution in enumerate(project_solutions):
            solution_project_name = project_solution.project
            solution_start_day = project_solution.start_day
            solution_end_day = project_solution.end_day

            for assignment in project_solution.assignment:
                solution_contributors = assignment.contributor
                solution_roles = assignment.role

                project_ind = projects.name.index(solution_project_name)
                project_roles = projects.role[project_ind]
                project_name = projects.name[project_ind]
                project_score = projects.score[project_ind]
                project_duration = projects.duration[project_ind]
                final_sccore =+ project_score
                for contributor_index, solution_contributor in enumerate(solution_contributors):
                    
                    contributor_ind = contributors.index(solution_contributor)
                    contributor_skill = contributors.skills[contributor_ind]
                    if project_roles[contributor_index].level <= contributor_skill:
                        continue
                    else:
                        print("project:{} need someone more skilled".format(project_name))
                        break

            
                    
                    
                    




                
                





    def promote(self, contributor):
        pass







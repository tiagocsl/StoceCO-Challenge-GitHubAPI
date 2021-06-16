from unittest import TestCase
from unittest.mock import patch

from src.resources import services
from src.resources.utils import Sorters, Returns_JSONs


class GitHubIntegrationTests(TestCase):    
    @patch("src.resources.services.mostPopularRepo")
    def test_get_popular_repository(self, MockPopularRepo):
        
        # Mockando o valor retornado da função mostPopularRepo
        MockPopularRepo.return_value = Returns_JSONs.return_value_popular_repo
        
        # Chamando a função mockada e ordenando por maior quantidade de estrela
        response = services.mostPopularRepo('gabrielclima')
        response.sort(key=Sorters.sortByStars, reverse=True)
        
        # Fazendo os asserts para confirmar se os resultados conferem com o esperado
        self.assertEqual("alfred", response[0]["repository_name"])
        self.assertGreater(response[0]["stargazers_count"], response[1]["stargazers_count"])
        MockPopularRepo.assert_called_with("gabrielclima")

    @patch("src.resources.services.mostCommentedIssue")
    def test_get_popular_issue(self, MockPopularIssue):

        # Mockando o valor retornado da função mostPopularIssue
        MockPopularIssue.return_value = Returns_JSONs.return_value_popular_issue

        # Chamando a função mockada e ordenando por maior quantidade de comentarios
        response = services.mostCommentedIssue("gabrielclima", "alfred")
        response.sort(key=Sorters.sortByComments, reverse=True)

        # Fazendo os asserts para confirmar se os resultados conferem com o esperado
        self.assertEqual("open", response[0]["state"])
        self.assertEqual(2, response[0]["number"])
        self.assertGreater(response[0]["comments"], response[1]["comments"])
        MockPopularIssue.assert_called_with("gabrielclima", "alfred")

    @patch("src.resources.services.uninteractedPull")
    def test_get_uninteracterd_pr(self, MockUninteractedPR):

        # Mockando o valor retornado da função mostPopularIssue
        MockUninteractedPR.return_value = Returns_JSONs.return_value_uninteracted_pull
       
        # Chamando a função mockada e ordenando por número em ordem crescente
        response = services.uninteractedPull("guilhermecstro", "solid-alura")
        response.sort(key=Sorters.sortByNumber)
        
        # Validando os dados que estão abertos 
        # no qual não foram comentados e nem revisados
        prToAssert = []
        for openPR in response:
            if openPR["state"] == "open" and openPR["reviews"] == 0 and openPR['comments'] == 0:
                prToAssert.append(openPR)

        # Fazendo os asserts para confirmar se os resultados conferem com o esperado
        for pr in prToAssert:
            self.assertEqual("open", pr["state"])
            self.assertEqual(0, pr["comments"])
            self.assertEqual(0, pr["reviews"])
        MockUninteractedPR.assert_called_with("guilhermecstro", "solid-alura")

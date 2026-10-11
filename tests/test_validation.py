"""Regression checks for publication failures that must block a release."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validate import ValidationError, load, validate_papers, valid_url


class PublicationValidationTests(unittest.TestCase):
    def setUp(self):
        self.papers=copy.deepcopy(load('data/papers.json'))
        self.snapshot=load('data/snapshot.json')

    def test_duplicate_identity_is_rejected(self):
        self.papers[1]['study_id']=self.papers[0]['study_id']
        with self.assertRaises(ValidationError):
            validate_papers(self.papers,self.snapshot)

    def test_private_field_is_rejected(self):
        self.papers[0]['local_file']='fulltext.pdf'
        with self.assertRaises(ValidationError):
            validate_papers(self.papers,self.snapshot)

    def test_unknown_role_is_rejected(self):
        self.papers[0]['solver_roles']=['R9']
        with self.assertRaises(ValidationError):
            validate_papers(self.papers,self.snapshot)

    def test_stale_population_is_rejected(self):
        with self.assertRaises(ValidationError):
            validate_papers(self.papers[:-1],self.snapshot)

    def test_credentials_and_nonweb_links_are_rejected(self):
        for url in ['https://user:pass@example.org/paper','file'+ ':///tmp/paper','https://example.org/?token=secret','javascript:alert(1)']:
            self.assertFalse(valid_url(url))
        self.assertTrue(valid_url('not_reported'))
        self.assertTrue(valid_url('https://doi.org/10.18653/v1/2023.findings-emnlp.248'))


if __name__=='__main__':
    unittest.main()

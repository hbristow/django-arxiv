# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.core.management import call_command

def load_fixtures(apps, schema_editor):
    """Load the initial arXiv subject groups into the database"""

    Subject = apps.get_model('arxiv', 'Subject')
    db = schema_editor.connection.alias
    Subject.objects.using(db).bulk_create([
        Subject(name="Statistics - Applications", cat="stat.AP"),
        Subject(name="Statistics - Computation", cat="stat.CO"),
        Subject(name="Statistics - Machine Learning", cat="stat.ML"),
        Subject(name="Statistics - Methodology", cat="stat.ME"),
        Subject(name="Statistics - Theory", cat="stat.TH"),
        Subject(name="Quantitative Biology - Biomolecules", cat="q-bio.BM"),
        Subject(name="Quantitative Biology - Cell Behavior", cat="q-bio.CB"),
        Subject(name="Quantitative Biology - Genomics", cat="q-bio.GN"),
        Subject(name="Quantitative Biology - Molecular Networks", cat="q-bio.MN"),
        Subject(name="Quantitative Biology - Neurons and Cognition", cat="q-bio.NC"),
        Subject(name="Quantitative Biology - Other", cat="q-bio.OT"),
        Subject(name="Quantitative Biology - Populations and Evolution", cat="q-bio.PE"),
        Subject(name="Quantitative Biology - Quantitative Methods", cat="q-bio.QM"),
        Subject(name="Quantitative Biology - Subcellular Processes", cat="q-bio.SC"),
        Subject(name="Quantitative Biology - Tissues and Organs", cat="q-bio.TO"),
        Subject(name="Computer Science - Architecture", cat="cs.AR"),
        Subject(name="Computer Science - Artificial Intelligence", cat="cs.AI"),
        Subject(name="Computer Science - Computation and Language", cat="cs.CL"),
        Subject(name="Computer Science - Computational Complexity", cat="cs.CC"),
        Subject(name="Computer Science - Computational Engineering; Finance; and Science", cat="cs.CE"),
        Subject(name="Computer Science - Computational Geometry", cat="cs.CG"),
        Subject(name="Computer Science - Computer Science and Game Theory", cat="cs.GT"),
        Subject(name="Computer Science - Computer Vision and Pattern Recognition", cat="cs.CV"),
        Subject(name="Computer Science - Computers and Society", cat="cs.CY"),
        Subject(name="Computer Science - Cryptography and Security", cat="cs.CR"),
        Subject(name="Computer Science - Data Structures and Algorithms", cat="cs.DS"),
        Subject(name="Computer Science - Databases", cat="cs.DB"),
        Subject(name="Computer Science - Digital Libraries", cat="cs.DL"),
        Subject(name="Computer Science - Discrete Mathematics", cat="cs.DM"),
        Subject(name="Computer Science - Distributed; Parallel; and Cluster Computing", cat="cs.DC"),
        Subject(name="Computer Science - General Literature", cat="cs.GL"),
        Subject(name="Computer Science - Graphics", cat="cs.GR"),
        Subject(name="Computer Science - Human-Computer Interaction", cat="cs.HC"),
        Subject(name="Computer Science - Information Retrieval", cat="cs.IR"),
        Subject(name="Computer Science - Information Theory", cat="cs.IT"),
        Subject(name="Computer Science - Learning", cat="cs.LG"),
        Subject(name="Computer Science - Logic in Computer Science", cat="cs.LO"),
        Subject(name="Computer Science - Mathematical Software", cat="cs.MS"),
        Subject(name="Computer Science - Multiagent Systems", cat="cs.MA"),
        Subject(name="Computer Science - Networking and Internet Architecture", cat="cs.NI"),
        Subject(name="Computer Science - Neural and Evolutionary Computing", cat="cs.NE"),
        Subject(name="Computer Science - Numerical Analysis", cat="cs.NA"),
        Subject(name="Computer Science - Other", cat="cs.OH"),
        Subject(name="Computer Science - Performance", cat="cs.PF"),
        Subject(name="Computer Science - Programming Languages", cat="cs.PL"),
        Subject(name="Computer Science - Robotics", cat="cs.RO"),
        Subject(name="Computer Science - Sound", cat="cs.SD"),
        Subject(name="Computer Science - Symbolic Computation", cat="cs.SC"),
        Subject(name="Nonlinear Sciences - Adaptation and Self-Organizing Systems", cat="nlin.AO"),
        Subject(name="Nonlinear Sciences - Cellular Automata and Lattice Gases", cat="nlin.CG"),
        Subject(name="Nonlinear Sciences - Chaotic Dynamics", cat="nlin.CD"),
        Subject(name="Nonlinear Sciences - Exactly Solvable and Integrable Systems", cat="nlin.SI"),
        Subject(name="Nonlinear Sciences - Pattern Formation and Solitons", cat="nlin.PS"),
        Subject(name="Mathematics - Algebraic Geometry", cat="math.AG"),
        Subject(name="Mathematics - Algebraic Topology", cat="math.AT"),
        Subject(name="Mathematics - Analysis of PDEs", cat="math.AP"),
        Subject(name="Mathematics - Category Theory", cat="math.CT"),
        Subject(name="Mathematics - Classical Analysis and ODEs", cat="math.CA"),
        Subject(name="Mathematics - Combinatorics", cat="math.CO"),
        Subject(name="Mathematics - Commutative Algebra", cat="math.AC"),
        Subject(name="Mathematics - Complex Variables", cat="math.CV"),
        Subject(name="Mathematics - Differential Geometry", cat="math.DG"),
        Subject(name="Mathematics - Dynamical Systems", cat="math.DS"),
        Subject(name="Mathematics - Functional Analysis", cat="math.FA"),
        Subject(name="Mathematics - General Mathematics", cat="math.GM"),
        Subject(name="Mathematics - General Topology", cat="math.GN"),
        Subject(name="Mathematics - Geometric Topology", cat="math.GT"),
        Subject(name="Mathematics - Group Theory", cat="math.GR"),
        Subject(name="Mathematics - History and Overview", cat="math.HO"),
        Subject(name="Mathematics - Information Theory", cat="math.IT"),
        Subject(name="Mathematics - K-Theory and Homology", cat="math.KT"),
        Subject(name="Mathematics - Logic", cat="math.LO"),
        Subject(name="Mathematics - Mathematical Physics", cat="math.MP"),
        Subject(name="Mathematics - Metric Geometry", cat="math.MG"),
        Subject(name="Mathematics - Number Theory", cat="math.NT"),
        Subject(name="Mathematics - Numerical Analysis", cat="math.NA"),
        Subject(name="Mathematics - Operator Algebras", cat="math.OA"),
        Subject(name="Mathematics - Optimization and Control", cat="math.OC"),
        Subject(name="Mathematics - Probability", cat="math.PR"),
        Subject(name="Mathematics - Quantum Algebra", cat="math.QA"),
        Subject(name="Mathematics - Representation Theory", cat="math.RT"),
        Subject(name="Mathematics - Rings and Algebras", cat="math.RA"),
        Subject(name="Mathematics - Spectral Theory", cat="math.SP"),
        Subject(name="Mathematics - Statistics", cat="math.ST"),
        Subject(name="Mathematics - Symplectic Geometry", cat="math.SG"),
        Subject(name="Astrophysics", cat="astro-ph"),
        Subject(name="Physics - Disordered Systems and Neural Networks", cat="cond-mat.dis-nn"),
        Subject(name="Physics - Mesoscopic Systems and Quantum Hall Effect", cat="cond-mat.mes-hall"),
        Subject(name="Physics - Materials Science", cat="cond-mat.mtrl-sci"),
        Subject(name="Physics - Other", cat="cond-mat.other"),
        Subject(name="Physics - Soft Condensed Matter", cat="cond-mat.soft"),
        Subject(name="Physics - Statistical Mechanics", cat="cond-mat.stat-mech"),
        Subject(name="Physics - Strongly Correlated Electrons", cat="cond-mat.str-el"),
        Subject(name="Physics - Superconductivity", cat="cond-mat.supr-con"),
        Subject(name="General Relativity and Quantum Cosmology", cat="gr-qc"),
        Subject(name="High Energy Physics - Experiment", cat="hep-ex"),
        Subject(name="High Energy Physics - Lattice", cat="hep-lat"),
        Subject(name="High Energy Physics - Phenomenology", cat="hep-ph"),
        Subject(name="High Energy Physics - Theory", cat="hep-th"),
        Subject(name="Mathematical Physics", cat="math-ph"),
        Subject(name="Nuclear Experiment", cat="nucl-ex"),
        Subject(name="Nuclear Theory", cat="nucl-th"),
        Subject(name="Physics - Accelerator Physics", cat="physics.acc-ph"),
        Subject(name="Physics - Atmospheric and Oceanic Physics", cat="physics.ao-ph"),
        Subject(name="Physics - Atomic Physics", cat="physics.atom-ph"),
        Subject(name="Physics - Atomic and Molecular Clusters", cat="physics.atm-clus"),
        Subject(name="Physics - Biological Physics", cat="physics.bio-ph"),
        Subject(name="Physics - Chemical Physics", cat="physics.chem-ph"),
        Subject(name="Physics - Classical Physics", cat="physics.class-ph"),
        Subject(name="Physics - Computational Physics", cat="physics.comp-ph"),
        Subject(name="Physics - Data Analysis; Statistics and Probability", cat="physics.data-an"),
        Subject(name="Physics - Fluid Dynamics", cat="physics.flu-dyn"),
        Subject(name="Physics - General Physics", cat="physics.gen-ph"),
        Subject(name="Physics - Geophysics", cat="physics.geo-ph"),
        Subject(name="Physics - History of Physics", cat="physics.hist-ph"),
        Subject(name="Physics - Instrumentation and Detectors", cat="physics.ins-det"),
        Subject(name="Physics - Medical Physics", cat="physics.med-ph"),
        Subject(name="Physics - Optics", cat="physics.optics"),
        Subject(name="Physics - Physics Education", cat="physics.ed-ph"),
        Subject(name="Physics - Physics and Society", cat="physics.soc-ph"),
        Subject(name="Physics - Plasma Physics", cat="physics.plasm-ph"),
        Subject(name="Physics - Popular Physics", cat="physics.pop-ph"),
        Subject(name="Physics - Space Physics", cat="physics.space-ph"),
        Subject(name="Quantum Physics", cat="quant-ph"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixtures),
    ]

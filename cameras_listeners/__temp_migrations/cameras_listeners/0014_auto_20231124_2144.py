# Generated by Django 2.2.12 on 2023-11-24 20:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras_listeners', '0013_auto_20231124_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='final',
        ),
        migrations.AddField(
            model_name='player',
            name='knowledge',
            field=otree.db.models.LongStringField(blank=True, null=True, verbose_name='<span style="line-height:1.7;font-size:18px">It is typically found in such studies that<b> much less than 90% of the intervals cover the actual number</b>. Of course, in some cases it can be bad luck, but given that this happens systematically, it is interpreted as what scholars call “overprecision”: many people tend to <b>overestimate the precision of their judgment</b>. This tendency has important consequences for the quality of decision-making in many domains. For example, it might make you underdiversify your investment portfolio ("put all your eggs in the same basket"). <b>If you are managing a project, you may underestimate the likelihood that it ends up taking much more time and money than expected</b>. See e.g., <a href="https://www.researchgate.net/profile/Elizabeth-Tenney/publication/316228342_Overprecision_in_Judgment/links/60abfb7b299bf1031fc843a8/Overprecision-in-Judgment.pdf" target="_blank">Overprecision in Judgment (Moore et al.)</a> to learn more (in particular, see section <em>Ecological Evidence of Overprecision</em> for some examples of real-life consequences of overprecision). For example, you will learn about the advantages and limitations of the kind of study you have just participated in.</span><span></span><span style="line-height:1.7;font-size:18px">Interestingly, many people guess that less than 90% of their intervals will cover the true values, probably intuiting their own overprecision.</span><p></p><span style="line-height:1.7;font-size:18px">If you have any (further) comments on the experiment, please make them below, ideally signing them. You can also contact me - Michal Krawczyk - directly via <a href = "mailto: michal.krawczyk@ec.europa.eu">e-mail</a> (e.g.if you want to provide your comments in a conversation -- that would be most helpful).'),
        ),
    ]

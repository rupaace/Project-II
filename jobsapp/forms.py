import profile
from django import forms

from jobsapp.models import Job, Applicant


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at','filled',)

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)

class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('user','created_at','job',)
        
    def is_valid(self):
        valid = super(ProfileCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        profile = super(ProfileCreateForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile
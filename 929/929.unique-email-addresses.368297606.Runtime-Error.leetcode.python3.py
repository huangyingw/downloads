class Solution:

    def numUniqueEmails1(self, emails):

        splited_eamils = [email.split('@') for email in emails]
        trans_emails = ['@'.join(email[0].split('+')[0].replace('.', '') + email[1]) for email in splited_eamils]
        return len(set(trans_emails))

    def numUniqueEmails2(self, emails):
        local_names = []
        for index, address in enumerate(emails):
            name = address.split('@')
            local_names.append(name[0].replace('.', '').split('+')[0] + '@' + name[1])
        return len(set(local_names))


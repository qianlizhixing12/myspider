// This is included with the Parsley library itself,
// thus there is no use in adding it to your project.
import Parsley from '../parsley/main';

Parsley.addMessages('en', {
    defaultMessage: "This value seems to be invalid.",
    type: {
        email: "这个不是有效邮箱!",
        url: "This value should be a valid url.",
        number: "This value should be a valid number.",
        integer: "This value should be a valid integer.",
        digits: "This value should be digits.",
        alphanum: "This value should be alphanumeric."
    },
    notblank: "This value should not be blank.",
    required: "这个值是必填项!",
    pattern: "This value seems to be invalid.",
    min: "This value should be greater than or equal to %s.",
    max: "This value should be lower than or equal to %s.",
    range: "This value should be between %s and %s.",
    minlength: "这个字符串太短, 至少需要 %s 个字符!",
    maxlength: "This value is too long. It should have %s characters or fewer.",
    length: "This value length is invalid. It should be between %s and %s characters long.",
    mincheck: "You must select at least %s choices.",
    maxcheck: "You must select %s choices or fewer.",
    check: "You must select between %s and %s choices.",
    equalto: "This value should be the same."
});

Parsley.setLocale('en');
